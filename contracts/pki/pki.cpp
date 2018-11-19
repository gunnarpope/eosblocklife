#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>

using namespace eosio;

class [[eosio::contract]] pki : public eosio::contract {

public:
  using contract::contract;


  pki(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}

  [[eosio::action]]
  void certify(name user, char pubkey, std::string algo, uint64_t expires) {
    require_auth( user );
    cert_index addresses(_code, _code.value);
    auto iterator = addresses.find(user.value);
    if( iterator == addresses.end() )
    {
      addresses.emplace(user, [&]( auto& row ) {
        row.Key = user;
        row.Pubkey = pubkey;
        row.Algo = algo;
        row.StartDate = current_time();
        row.EndDate = expires;
      });
    }
    else {
      addresses.modify(iterator, user, [&]( auto& row ) {
        row.Key = user;
        row.Pubkey = pubkey;
        row.Algo = algo;
        row.StartDate = current_time();
        row.EndDate = expires;
      });
    }
  }

  [[eosio::action]]
  void erase(name user) {
    require_auth(user);

    cert_index addresses(_self, _code.value);

    auto iterator = addresses.find(user.value);
    eosio_assert(iterator != addresses.end(), "Record does not exist");
    addresses.erase(iterator);
  }

private:
  struct [[eosio::table]] cert {
    name Key;
    char Pubkey;
    std::string Algo;
    uint64_t StartDate;
    uint64_t EndDate;
    uint64_t primary_key() const { return Key.value; }
  };
  typedef eosio::multi_index<"certificates"_n, cert> cert_index;

};

EOSIO_DISPATCH( pki, (certify)(erase))
