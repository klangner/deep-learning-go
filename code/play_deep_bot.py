from dlgo.agent.predict import DeepLearningAgent, load_prediction_agent
from dlgo.httpfrontend.server import get_web_app
import h5py


model_file = h5py.File("agents/deep_bot.h5", "r")
bot_from_file = load_prediction_agent(model_file)

web_app = get_web_app({'predict': bot_from_file})
web_app.run()
