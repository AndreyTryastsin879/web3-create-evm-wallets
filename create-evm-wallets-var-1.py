from web3 import Web3
import pandas as pd

ACCOUNTS_QUANTITY = 10

connection = Web3()

list_of_dicts = []
for number in range(ACCOUNTS_QUANTITY):
    account = connection.eth.account.create()
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

writer_kernel = pd.ExcelWriter('ready_evm_accounts_var_1.xlsx', engine='xlsxwriter')
df.to_excel(writer_kernel, index=False)
writer_kernel.close()

# export to txt
with open('ready_evm_accounts_var_1.txt', 'w') as file:
    for d in list_of_dicts:
        file.write(f"{d['address']},{d['private_key']}\n")
