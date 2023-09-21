from web3 import Web3
import pandas as pd

ACCOUNTS_QUANTITY = 10

connection = Web3()

connection.eth.account.enable_unaudited_hdwallet_features()

list_of_dicts = []
for number in range(ACCOUNTS_QUANTITY):
    account = connection.eth.account.create_with_mnemonic()
    seed_phrase = account[1]
    address = account[0].address
    private_key = account[0].key.hex()

    print('Account', number + 1, '\n',
          'Seed:', seed_phrase, '\n',
          'Public:', address, '\n',
          'Private_key:', private_key, '\n',
          '--------------------------')

    dictionary = dict()
    dictionary['seed_phrase'] = seed_phrase
    dictionary['address'] = address
    dictionary['private_key'] = private_key

    list_of_dicts.append(dictionary)

# export to excel
df = pd.DataFrame.from_dict(list_of_dicts)

writer_kernel = pd.ExcelWriter('ready_evm_accounts_var_2.xlsx', engine='xlsxwriter')
df.to_excel(writer_kernel, index=False)
writer_kernel.close()

# export to txt
with open('ready_evm_accounts_var_2.txt', 'w') as file:
    for d in list_of_dicts:
        file.write(f"{d['seed_phrase']},{d['address']},{d['private_key']};\n")
