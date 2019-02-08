from dlgo.agent.predict import DeepLearningAgent, load_prediction_agent
from dlgo.httpfrontend.server import get_web_app
import h5py
from dlgo import goboard_fast as goboard 


model_file = h5py.File("agents/deep_bot.h5", "r")
deep_bot = load_prediction_agent(model_file)
deep_bot.model._make_predict_function()
web_app = get_web_app({'predict': deep_bot})
web_app.run()
