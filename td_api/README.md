# Scoreboard API Deployment

I've built this API using FastAPI and I've deployed it on [https://deta.sh/](https://deta.sh/) for FREE !  
If you want to do the same you need to:

- Create an account on deta.sh
- Create a project token and save it inside this folder under the `.env` file as `DETAKEY=<your_token>`
- Run `curl -fsSL https://get.deta.dev/cli.sh | sh` to install the deta CLI.
- Run `deta update -e .env` to add the env variables to Deta.
- Run `deta new` for Deta to run your API. You will get an URL, this will be your API URL. (Or `deta deploy` if you already deployed one and you just want to deploy changes !)
  You can visit <your_url>/docs to get the Swagger info of your API.  
  Don't forget to change the URL in the Notebook in `show_leaderboard` and `send_my_score` function with your own API url.

Enjoy :)

Tip: visit [https://web.deta.sh/](https://web.deta.sh/) to manage your database and API easily !
