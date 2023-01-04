import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key("Kd7ca2gykKScsNHZQ989gaBpSEthj4pHuvX7HHpEwr8")

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def emotion_analysis(self,text):
        response = paralleldots.emotion(text)
        return response
        
    def abuse_analysis(self,text):
        response = paralleldots.abuse(text)
        return response

    