# demo-app

A deliberately-broken sample app used to demo the
[Pipeline Reviewer Agent](https://github.com/NavyaSivakoti/pipeline-reviewer).

`test_charge_eur` fails on purpose (the code ignores the `currency` argument), so
CI goes red — and the **AI Pipeline Reviewer** runs automatically and comments
the review (root cause + suggested fix) on the commit/PR.

See `.github/workflows/ci.yml`.

<!-- trigger PR CI demo -->
