### Fxshop

FX Shop - Simplified Currency/Exchange transactions on top of ERPNext (required dependency)

Only 2 DocTypes so far: -

1) Exchange Transactions - Treats each currency (USD, EUR, AED, etc..) as stock so that gross profit per transaction can be known using either FIFO/LIFO/AVCO method. May not be in line with IAS 2/21 or IFRS 9
2) Partner Transfer - Nostro/Vostro transactions done by partners in other countries

Let me know on Telegram (https://t.me/Asieftejani) or emal (asief.tejanI@gmail.com) if you are interested in developing it further according to your needs

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench install-app fxshop
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/fxshop
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
