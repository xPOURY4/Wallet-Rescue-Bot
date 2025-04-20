# 🔐 Multi-Chain Wallet Rescue Bot

Rescue both native (ETH, BNB, etc.) and ERC-20 tokens from compromised wallets securely and automatically. This bot supports multiple EVM-compatible blockchains and periodically scans wallet balances every 30 seconds.

---

## 🌍 Supported Networks

- Ethereum
- BNB Smart Chain (BSC)
- Polygon
- Arbitrum
- Optimism
- Fantom
- Base
- Gravity
- Sonic
- Soneium
- Zora

---

## ✨ Features

- ✅ Supports multiple wallets and multiple chains
- ✅ Automatically transfers native and ERC-20 tokens
- ✅ Smart gas fee buffer to avoid transaction failures
- ✅ Periodic scanning every 30 seconds
- ✅ Logs all transactions and errors

---

## ⚙️ Installation & Configuration

### 1. Clone the Repository
```bash
git clone https://github.com/xPOURY4/wallet-rescue-bot.git
cd wallet-rescue-bot
```

### 2. Install Dependencies
```bash
pip install web3
```

### 3. Configure Wallets
Edit the `wallets` list inside `main.py`:
```python
wallets = [
  {
    'private_key': 'YOUR_PRIVATE_KEY',
    'from_address': Web3.to_checksum_address('0xYourWallet'),
    'safe_address': Web3.to_checksum_address('0xYourSafeWallet')
  },
  # Add more wallets if needed
]
```

### 4. Configure Tokens
Update the `tokens` list to include your desired ERC-20 tokens:
```python
tokens = [
  {'symbol': 'USDC', 'address': '0x...'},
  {'symbol': 'DAI', 'address': '0x...'},
  # Add more tokens
]
```

### 5. Run the Bot
```bash
python main.py
```

---

## 🧠 How It Works

- ⛽ Scans ERC-20 token balances and transfers them to the safe address.
- 💸 Transfers the remaining native token (e.g. ETH) minus gas fees.

---

## 📝 Logging

All activity is saved to `log.txt`, including successful and failed transactions.

---

## 🤝 Contributing

Pull requests are welcome to improve this tool.

---

## ⚠️ Disclaimer

> This tool is intended for emergency fund recovery only. Do not expose or share your private keys under any circumstances.

---

> Built by [@xPOURY4](https://github.com/xPOURY4)

---

# 🔐 بات نجات کیف‌پول چندشبکه‌ای

این بات پایتونی برای نجات خودکار توکن‌های بومی (مثل ETH، BNB) و توکن‌های ERC-20 از کیف‌پول‌های هک‌شده در شبکه‌های مختلف EVM طراحی شده و هر ۳۰ ثانیه کیف‌پول‌ها را بررسی کرده و در صورت وجود موجودی، به آدرس امن انتقال می‌دهد.

---

## 🌍 شبکه‌های پشتیبانی‌شده

- اتریوم
- زنجیره هوشمند BNB
- پالیگان
- آربیتروم
- آپتیمیسم
- فانتوم
- بیس (Base)
- گراویتی
- سونیک
- سونیوم
- زورا

---

## ✨ امکانات

- ✅ پشتیبانی از چندین کیف‌پول و شبکه
- ✅ انتقال خودکار توکن‌های بومی و ERC-20
- ✅ محاسبه هوشمند کارمزد برای جلوگیری از خطا
- ✅ اسکن خودکار هر ۳۰ ثانیه
- ✅ ثبت همه لاگ‌ها و خطاها در فایل

---

## ⚙️ مراحل نصب و راه‌اندازی

### 1. دریافت پروژه
```bash
git clone https://github.com/xPOURY4/wallet-rescue-bot.git
cd wallet-rescue-bot
```

### 2. نصب پیش‌نیازها
```bash
pip install web3
```

### 3. تنظیم کیف‌پول‌ها
فایل `main.py` را باز کرده و مقادیر زیر را ویرایش کنید:
```python
wallets = [
  {
    'private_key': 'کلید خصوصی شما',
    'from_address': Web3.to_checksum_address('آدرس کیف‌پول شما'),
    'safe_address': Web3.to_checksum_address('آدرس کیف‌پول امن شما')
  },
  # می‌توانید کیف‌پول‌های بیشتری اضافه کنید
]
```

### 4. تنظیم توکن‌ها
در همان فایل، لیست `tokens` را با توکن‌های مورد نظر به‌روزرسانی کنید:
```python
tokens = [
  {'symbol': 'USDC', 'address': '0x...'},
  {'symbol': 'DAI', 'address': '0x...'},
  # توکن‌های بیشتر اضافه کنید
]
```

### 5. اجرای بات
```bash
python main.py
```

---

## 🧠 نحوه عملکرد

- ابتدا همه توکن‌های ERC-20 موجود را به آدرس امن منتقل می‌کند.
- سپس باقیمانده توکن گس (مثلاً ETH یا BNB) را منهای کارمزد انتقال می‌دهد.

---

## 📝 ثبت لاگ

همه فعالیت‌ها، از جمله موفق یا ناموفق، در فایل `log.txt` ذخیره می‌شوند.

---

## 🤝 مشارکت

برای ارتقاء این پروژه، Pull Request ارسال کنید 🙌

---

## ⚠️ هشدار امنیتی

> این ابزار فقط برای مواقع اضطراری طراحی شده است. لطفاً کلید خصوصی خود را به‌هیچ‌وجه منتشر نکنید یا در اختیار دیگران قرار ندهید.

---

> توسعه داده‌شده توسط [@xPOURY4](https://github.com/xPOURY4) ❤️
