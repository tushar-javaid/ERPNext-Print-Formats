<h1 align="center">🧾 ERPNext Print Formats</h1>

<p align="center">
  <img src="https://img.shields.io/badge/ERPNext-Compatible-blue?style=flat-square&logo=erpnext" alt="ERPNext Compatible Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License Badge"/>
  <img src="https://img.shields.io/badge/Version-Develop-orange?style=flat-square" alt="Version Badge"/>
</p>

<p align="center">
  <b>Reusable, beautiful print formats for ERPNext / Frappe 💼</b><br>
  <i>Save time by using ready-to-go Payment and Receiving Vouchers for your ERP system.</i>
</p>

---

### ✨ ERPNext Print Formats

ERPNext Print Formats

---

### ⚙️ Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app erpnext_print_formats
````

<p align="center">
  <img src="https://raw.githubusercontent.com/frappe/erpnext/develop/erpnext/public/images/erpnext-logo.png" alt="ERPNext Logo" width="200"/><br>
  <i>Install easily in any Frappe/ERPNext bench.</i>
</p>

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
* ⚡ **pyupgrade**

<p align="center">
  <img src="https://raw.githubusercontent.com/pre-commit/pre-commit.com/main/logo.png" width="120" alt="pre-commit logo"/><br>
  <i>Automatic linting and style enforcement keeps your code consistent.</i>
</p>

---

### 🧪 CI (Continuous Integration)

This app can use **GitHub Actions** for CI.
The following workflows are configured:

* 🧩 **CI:** Installs this app and runs unit tests on every push to `develop` branch.
* 🧹 **Linters:** Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

<p align="center">
  <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="80" alt="GitHub Logo"/><br>
  <i>Automated quality checks on every commit & pull request.</i>
</p>

---

### 🪪 License

**MIT License**

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT Badge"/><br>
  <i>Open source. Free to use, modify, and share.</i>
</p>

---

<h2 align="center">📸 Example Visuals</h2>

<p align="center">
  <img src="https://via.placeholder.com/900x500.png?text=Payment+Voucher+Print+Preview" alt="Payment Voucher Print Format Preview" width="85%"/><br><br>
  <i>Example: Payment Voucher print format as seen inside ERPNext.</i>
</p>

---

<h2 align="center">💡 Key Highlights</h2>

<p align="center">
  <img src="https://via.placeholder.com/900x200.png?text=Reusable+Print+Formats+Overview" alt="ERPNext Print Format Overview" width="80%"/>
</p>

* ✅ **Ready-to-use** print formats for Payment & Receiving Vouchers
* 🧱 Built using **Jinja** + ERPNext’s native Print Format Builder
* 🧩 **Easy customization** via JSON or UI editor
* 🪶 Lightweight — no extra dependencies, just print formats

---

<h2 align="center">🚀 Quick Start</h2>

```bash
# from your bench folder
bench get-app $URL_OF_THIS_REPO --branch develop
bench --site your-site-name install-app erpnext_print_formats
bench --site your-site-name migrate
```

After installation, find the print formats under **Setup → Print Format** in ERPNext.

---

<h2 align="center">🧰 Troubleshooting</h2>

| Issue                        | Possible Fix                                                |
| ---------------------------- | ----------------------------------------------------------- |
| ❌ Print formats not visible  | Run `bench --site your-site-name migrate` and `clear-cache` |
| 🧾 Layout looks wrong in PDF | Ensure **wkhtmltopdf** is installed                         |
| 🎨 CSS not applied           | Check `public/css` or inline styles in print format         |

---

<h2 align="center">👨‍💻 Developer Notes</h2>

* **Pre-commit hooks:** run `pre-commit install` inside the app folder.
* **CI:** GitHub Actions automate testing & linting.
* **Key paths:**

  * `erpnext_print_formats/fixtures/print_format.json`
  * `templates/` and `public/` folders for your assets.

---

<h2 align="center">🌍 Contribute & Collaborate</h2>

1. 🍴 Fork the repository
2. 🌱 Create your feature branch
3. 🧩 Add your print format or improvements
4. ✅ Run pre-commit checks
5. 🚀 Open a Pull Request

<p align="center">
  <img src="https://img.shields.io/badge/Contributions-Welcome-blueviolet?style=for-the-badge" alt="Contributions Welcome"/>
</p>

---

<p align="center">
  <b>🎉 Thank you for using ERPNext Print Formats!</b><br>
  <i>Save time, print beautifully, and keep your ERP clean.</i>
</p>

---
