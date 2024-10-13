from web3 import Web3

# 连接到以太坊主网（使用 Alchemy 或 Infura 的 URL）
provider_url = 'https://eth-mainnet.g.alchemy.com/v2/REnJpS0IE8fF-4T3yNUiI7z9SBiTpV1'
w3 = Web3(Web3.HTTPProvider(provider_url))

# 检查连接状态
if w3.isConnected():
    print("成功连接到以太坊主网")
else:
    print("连接失败")

# 设置钱包地址（你可以替换成你自己的地址）
wallet_address = '0xYourWalletAddress'

# 查询钱包余额
balance = w3.eth.get_balance(wallet_address)

# 将余额从 Wei 转换为以太币 (ETH)
eth_balance = w3.fromWei(balance, 'ether')

print(f"地址 {wallet_address} 的余额为: {eth_balance} ETH")
