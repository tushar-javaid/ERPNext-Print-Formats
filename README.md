<div align="center">

# 🧾 ERPNext Print Formats  
### Reusable, Polished Print Templates for ERPNext & Frappe  

<img src="https://raw.githubusercontent.com/frappe/erpnext/develop/erpnext/public/images/erpnext-logo.png" alt="ERPNext Logo" width="180"/>

</div>

---

## ✨ Overview  

> **ERPNext Print Formats** is a lightweight Frappe app providing ready-made, reusable **print templates** for documents like Payment and Receiving Vouchers.  
> Simplify your ERP workflow — no need to design formats from scratch.  

---

### ERPNext Print Formats  

ERPNext Print Formats  

---

### 🧩 Installation  

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app erpnext_print_formats
````

<div align="center">
<img src="https://img.shields.io/badge/ERPNext-Compatible-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Frappe-Framework-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge" />
</div>

---

### 🤝 Contributing

This app uses `pre-commit` for code formatting and linting.
Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/erpnext_print_formats
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

* 🐍 **ruff**
* 💅 **eslint**
* 🎨 **prettier**
* ⚙️ **pyupgrade**

---

### ⚙️ CI

This app can use GitHub Actions for CI.
The following workflows are configured:

* 🧪 **CI:** Installs this app and runs unit tests on every push to `develop` branch.
* 🔍 **Linters:** Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

---

### 🪪 License

**MIT**

---

<div align="center">
<img src="erpnext_print_formats/assets/Payment Voucher.png" alt="ERPNext Print Preview" width="80%"/>
<p><em>Example Print Format — Payment Voucher</em></p>
</div>

---

## 💡 About this App

This small app contains reusable **Print Formats for ERPNext / Frappe**.
It provides ready-made, easy-to-use templates like:

* 🧾 **Payment Voucher**
* 📥 **Receiving Voucher**

The goal: **Save time.** No need to build formats manually.

---

## 🔑 Key Features

✅ Ready-to-use print formats for common documents
✅ Jinja-based templates that integrate with ERPNext’s Print Format builder
✅ Easy to customize via JSON or UI
✅ Focused and minimal — no extra logic

---

## 📂 What's Included

```
fixtures/print_format.json   →  JSON definitions of all included print formats
templates/, public/          →  Add custom HTML/CSS/JS if needed
```

**Included formats:**

* "Payment Voucher" — shows paid amount, party, and bank details.
* "Receiving Voucher" — for incoming payments.

---

## ⚡ Quick Installation

Follow these simple steps:

```bash
# Step 1: Fetch the app
bench get-app $URL_OF_THIS_REPO --branch develop

# Step 2: Install on your site
bench --site your-site-name install-app erpnext_print_formats
bench --site your-site-name migrate
```

After this, you’ll see new formats in the **Print Format** list inside ERPNext.

---

## 🧭 How to Use

1. Log in as Administrator (or any user with Print Format rights).
2. Navigate to: **Setup → Print Format**.
3. Open “Payment Voucher” or “Receiving Voucher”.
4. Open a Payment Entry → click **Print** → choose your format.

<div align="center">
<img src="erpnext_print_formats/assets/Print Format Selection.png" alt="Print Format Selection" width="70%"/>
</div>

---

## 🧰 Customizing Print Formats

**Option A — Using Print Format Builder (No-Code)**

1. Open the format in ERPNext.
2. Click “Edit with Print Format Builder”.
3. Rearrange fields, change styles, and save.

**Option B — Editing Fixture JSON (For Developers)**

1. Modify `erpnext_print_formats/fixtures/print_format.json`.
2. Commit and apply changes:

```bash
git add erpnext_print_formats/fixtures/print_format.json
git commit -m "Update Payment Voucher format"
bench --site your-site-name migrate
```

🧠 **Tip:** Always back up before running migrations.

---

## 🧑‍💻 Developer Notes

* `pre-commit` hooks ensure clean, consistent code.
* `CI` runs automated tests and linting.
* Key paths:

  * `erpnext_print_formats/fixtures/print_format.json` — fixtures
  * `templates/`, `public/` — static assets

---

## 🩺 Troubleshooting

| Issue                       | Fix                                                               |
| --------------------------- | ----------------------------------------------------------------- |
| ❌ Print formats not visible | Run `bench --site your-site install-app ...` then `bench migrate` |
| 🧾 PDF layout broken        | Ensure `wkhtmltopdf` (v0.12.x patched Qt) is installed            |
| 🎨 CSS not applied          | Check `public/css` or use inline `<style>` in the Print Format    |

---

## 🚀 Try It Quickly

```bash
bench get-app $URL_OF_THIS_REPO --branch develop
bench --site your-site-name install-app erpnext_print_formats
bench --site your-site-name migrate
```

---

## 🧱 Contributing

Want to help? Fork, improve, and open a PR.

1. Create a feature branch
2. Run `pre-commit` before committing
3. Open a PR with a clear title (e.g. “Add Purchase Order Format”)

---

<div align="center">

### 🏁 License

**MIT License**

<img src="https://img.shields.io/github/license/frappe/frappe?style=for-the-badge" />

---

### 💬 Feedback & Ideas

💡 Have an idea for a new format? Open an Issue or Discussion!

</div>

---