from web3 import Web3
import pandas as pd

ACCOUNTS_QUANTITY = 10

connection = Web3()

connection.eth.account.enable_unaudited_hdwallet_features()

mnemonic = connection.eth.account.create_with_mnemonic()[1]

list_of_dicts = []
for number in range(ACCOUNTS_QUANTITY):
    account = connection.eth.account.from_mnemonic(mnemonic,
                                                   account_path=f"m/44'/60'/0'/0/{number}")
    address = account.address
    private_key = account.key.hex()

    print('Account', number + 1, '\n',
          'Public:', address, '\n',
          'Private_key:', private_key, '\n',
          '--------------------------')

    dictionary = dict()
    dictionary['address'] = address
    dictionary['private_key'] = private_key

    list_of_dicts.append(dictionary)

# export to excel
df = pd.DataFrame.from_dict(list_of_dicts)

writer_kernel = pd.ExcelWriter('ready_evm_accounts_var_3.xlsx', engine='xlsxwriter')
df.to_excel(writer_kernel, index=False)
writer_kernel.close()

# export to txt
with open('ready_evm_accounts_var_3.txt', 'w') as file:
    for d in list_of_dicts:
        file.write(f"{d['address']},{d['private_key']};\n")

# Another example of export
# export to excel
df = pd.DataFrame.from_dict(list_of_dicts)
df['seed'] = mnemonic

pivot_df = df.pivot_table(index=['seed', 'address', 'private_key'])

writer_kernel = pd.ExcelWriter('ready_evm_accounts_var_3_global_seed.xlsx', engine='xlsxwriter')
pivot_df.to_excel(writer_kernel)
writer_kernel.close()

# export to txt
with open('ready_evm_accounts_var_3_global_seed.txt', 'w') as file:
    file.write(f'{mnemonic}, \n --------------- \n \n')
    for d in list_of_dicts:
        file.write(f"{d['address']},{d['private_key']};\n")
