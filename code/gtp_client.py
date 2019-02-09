from dlgo.gtp import GTPFrontend
from dlgo.agent.predict import load_prediction_agent
from dlgo.agent import termination
import h5py


bot = load_prediction_agent(h5py.File("agents/deep_bot.h5", "r"))
strategy = termination.get("opponent_passes")
termination_agent = termination.TerminationAgent(bot, strategy)
frontend = GTPFrontend(termination_agent)
frontend.run()