# Swap

## What does it do?

Swap offers automation for finance departments that work with Supervielle.SA bank extracts allowing them to quickly obtain
- Third party transfers summary by CUIL
- Taxes applied to each extract category

## How to use it

Swap its a fast api project that uses poetry for its setup.

1) Install poetry in your environment
2) Run poetry install 
3) Place your extracts at the `extractos/` folder
4) Mount the project by doing `poetry run uvicorn main:app --reload`
5) Head to `http://localhost:8000/banks/supervielle/<your_companies_cuil>`
6) Check your applied taxes at `taxes/supervielle.json`
7) Check your transfers at  `transfers/supervielle.json`


## Future work

- [ ] Change the resulting json files to be named such as `supervielle_{timestamp}.json`
- [ ] Specify which extract you wanna process
- [ ] Allow users to upload the extract through a web interface

