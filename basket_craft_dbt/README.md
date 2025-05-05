This project builds an end-to-end analytics pipeline for basket_craft. I extracted website session data for December 2023 from a MySQL source, loaded it into a raw Postgres schema, and transformed it using dbt into staging and warehouse models. A GitHub Actions workflow automated the ELT job using secrets for secure access. The final model, `fct_website_sessions_utm_source_daily`, powers a Looker Studio dashboard with interactive filtering, trend analysis, and repeat session insights by UTM source. 



