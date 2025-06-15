import requests, random
from Helper import constants
from News.models import News, Template

class Facebook:
    def __init__(self, user_access_token=None, page_id=None, page_access_token=None):
        self.page_id = page_id
        self.page_access_token = page_access_token
        self.user_access_token = user_access_token
        self.url = f"https://graph.facebook.com/v19.0/{page_id}/photos"

        if not page_id:
            raise Exception("Please provide a valid page ID!")
        # if not user_access_token:
        #     raise Exception("Please provide a valid user access token!")
        if not page_access_token:
            raise Exception("Please provide a valid page access token!")

    def print_all_account(self):
        url = f"https://graph.facebook.com/v19.0/me/accounts?access_token={self.user_access_token}"
        res = requests.get(url)
        accounts = res.json()['data']
        

        for account in accounts:
            print("^_^_"*35)
            print("Page Name: ", account['name'], "Page ID: ", account['id'])
            print("Page Token: ", account['access_token'])

        print("^_^_"*35)

    def print_response(self, response, type="Text"):
        if response.status_code == 200:
            print(f"✅ {type} posted successfully!")
            print("📌 Post ID:", response.json().get('post_id'))
        else:
            print(f"❌ Failed to post {type}.")
            print("📄 Status Code:", response.status_code)
            print("📄 Response:", response.text)

    def post_text_to_page(self, message="Post from Python"):
        url = f'https://graph.facebook.com/v19.0/{self.page_id}/feed'
        payload = {
            'message': message,
            'access_token': self.page_access_token
        }
        response = requests.post(url, data=payload)
        self.print_response(response)

    def post_online_image_to_page(self, image_url=None, caption="Post from Python"):
        if not image_url: 
            return "Please provide an image url from online!"
        payload = {
            'url': image_url,
            'caption': caption,
            'access_token': self.page_access_token
        }
        response = requests.post(self.url, data=payload)
        self.print_response(response, type="Online Image")

    def post_local_image_to_page_working(self, image_path=None, caption="Post from Python Local Image"):
        if not image_path: 
            return "Please provide an image url from local!"
        files = {
            'source': open(image_path, 'rb')
        }
        payload = {
            'caption': caption,
            'access_token': self.page_access_token
        }
        response = requests.post(self.url, files=files, data=payload)
        self.print_response(response, type="Local Image")

    def comment_on_post(self, post_id=None, comment="Comment from Python"):
        if not post_id: 
            return "Please provide a post id!"
        url = f'https://graph.facebook.com/v19.0/{post_id}/comments'
        payload = {
            'message': comment,
            'access_token': self.page_access_token
        }
        response = requests.post(url, data=payload)

    def post_local_image_to_page(self, image_path=None, caption="Post from Python Local Image"):
        if not image_path: 
            return "Please provide an image url from local!"
        files = {
            'source': open(image_path, 'rb')
        }
        payload = {
            'caption': caption,
            'access_token': self.page_access_token,
            'published': True,
        }
        response = requests.post(self.url, files=files, data=payload)
        self.print_response(response, type="Local Image")
        return response
    
    def request_to_post_gemten(data):
        url = 'http://127.0.0.1:8000/api/post/to/facebook/'
        res = requests.post(url, json=data)

        response = res.json()
        return response
    
    def post_to_Gemten_News_page(news_id):
        from Helper.helpers import Helper
        template_id = Helper.get_random_one_page_template_id(constants.GEMTEN_NEWS_PAGE_ID)
        data = {
            'id': news_id, # News Id
            'template_id': template_id, # Template Id
            'storedPages': '['
                '{"pageId": "571480596045760",'
                '"accessToken": "EAA7ctFADgFIBOxfbuDy4Hju1YfqZAr9aHWhIlnsdbhaCnkCJmeIDjWq52OPZBVO7awCb0lWmcPJ5WXRWuWir4MrACSJQAcxN6dASsuFPXjMsczkPygYeqno6sznUdA3AQjjMNPtELp9ZALWWdP0jaKOPfvgZAsc8j2dnptv1yFWRdJh6LEReukNFRGx0LF8q05INZBkCoMZALLXxi74wjp",'
                '"categories": ["Sports", "Entertainment", "Technology", "World", "Bangladesh", "Science", "Economy", "City News", "TechStartup", "Islam", "National", "Politics", "Business", "Health"]''}'
            ']'
        }

        response = Facebook.request_to_post_gemten(data)
        return response
    
    def post_to_Gemten_Terabyte_page(news_id):
        from Helper.helpers import Helper
        template_id = Helper.get_random_one_page_template_id(constants.GEMTEN_TERABYTE_PAGE_ID)
        data = {
            'id': news_id, # News Id
            'template_id': template_id, # Template Id
            'storedPages': '['
                '{"pageId": "644657182073016",'
                '"accessToken": "EAA7ctFADgFIBO4WlpmXFJxI2UeY4SZC1fs1oZAZA9oE8U4i1cnOebWavHXvmYZBVvezZAqNnjvOWm73viZAPaKZCHYzEEB3lit2APbZBU4UHmDqfZBvBkaTCWcF1bq5TEZAarLhdON5MbmQPZCmoZCsZBkFuFi6OmQfR3HzZAjfxDqMRuHnhWdSz9MwhJp1DpVPDdqMK0CyeOLOEJs4VikxdQ5C0i6",'
                '"categories": ["Sports", "Entertainment", "Technology", "World", "Bangladesh", "Science", "Economy", "City News", "TechStartup", "Islam", "National", "Politics", "Business", "Health"]''}'
            ']'
        }

        response = Facebook.request_to_post_gemten(data)
        return response
    
    def post_to_Gemten_Cricket_page(news_id):
        from Helper.helpers import Helper
        template_id = Helper.get_random_one_page_template_id(constants.GEMTEN_CRICKET_PAGE_ID)
        data = {
            'id': news_id, # News Id
            'template_id': template_id, # Template Id
            'storedPages': '['
                '{"pageId": "463298220210795",'
                '"accessToken": "EAA7ctFADgFIBO4UFgxrWAAfYUND2I0T0gbU4zZAvfwonwDyY1RXv1QEiO0LS6vHU9y07zjKJW6aNg8debrG74ErYNLIys95ZCyryGqCktZAxZCxSa0R48K2DJNDdFE3ZAdQGbiVAZCMUvcq1HK5c1hDKRGZByAaZBX6ejvpmv4PfvIq5MNd2YZCjOuNZAYZAokjZAyXTd7OpYJt1UB5XVIiYDxVG",'
                '"categories": ["Sports", "Entertainment", "Technology", "World", "Bangladesh", "Science", "Economy", "City News", "TechStartup", "Islam", "National", "Politics", "Business", "Health"]''}'
            ']'
        }

        response = Facebook.request_to_post_gemten(data)
        return response
    
    def post_to_Gemten_Sports_page(news_id):
        from Helper.helpers import Helper
        template_id = Helper.get_random_one_page_template_id(constants.GEMTEN_SPORTS_PAGE_ID)
        data = {
            'id': news_id, # News Id
            'template_id': template_id, # Template Id
            'storedPages': '['
                '{"pageId": "692806730579545",'
                '"accessToken": "EAATSp6m0zA8BO0OK9R7tX1bhwZBz2ravzRLIIwh1PKwHi2YdQbVtTJ7cO2QvBnQy8WxkqfO1EnLZA9NyMW9f70d5odCcVmYYZABv2ZCSvD26ugkifIqN2jZCuZB5vOMEDMR4dh6gPwXaEYQEuIg3GT0kA3qR4MegS1GTVm3QtIHoxxel7sQVycEZCZCJDZAKzi6FMJdDQ2qEk",'
                '"categories": ["Sports", "Entertainment", "Technology", "World", "Bangladesh", "Science", "Economy", "City News", "TechStartup", "Islam", "National", "Politics", "Business", "Health"]''}'
            ']'
        }

        response = Facebook.request_to_post_gemten(data)
        return response
    
    def post_to_Gemten_ESports_page(news_id):
        from Helper.helpers import Helper
        template_id = Helper.get_random_one_page_template_id(constants.GEMTEN_ESPORTS_PAGE_ID)
        data = {
            'id': news_id, # News Id
            'template_id': template_id, # Template Id
            'storedPages': '['
                '{"pageId": "460605427136929",'
                '"accessToken": "EAA7ctFADgFIBOxwL6MWrScHF6GkC6fBlZBgYzYjGmgkCvaXzSua7FKFs4efIEJ1FIwfw5kMOYiXgtEoOzBPMZAYuwAk7vsCJm8DFhmnOKEFPYVhcr6hSz2QqAdmByMIoSbZBoBcD5YlT0Lw12V24lZCbC1n2p0730Wd6BHtk4OtO8eyVLOgEzA2OHoBcYDVaIRx3WlNAb0ZBxSXVcAKutDxe3",'
                '"categories": ["Sports", "Entertainment", "Technology", "World", "Bangladesh", "Science", "Economy", "City News", "TechStartup", "Islam", "National", "Politics", "Business", "Health"]''}'
            ']'
        }

        response = Facebook.request_to_post_gemten(data)
        return response
    
    def post_to_Gemten_Football_page(news_id):
        from Helper.helpers import Helper
        template_id = Helper.get_random_one_page_template_id(constants.GEMTEN_FOOTBALL_PAGE_ID)
        data = {
            'id': news_id, # News Id
            'template_id': template_id, # Template Id
            'storedPages': '['
                '{"pageId": "684520311406135",'
                '"accessToken": "EAATSp6m0zA8BOZCaQXZCN6QcMtZBwfZCSnw2Xmum17aCOCpVuAE7KqdZAGPu1RBTG6TCZC4LbL9MkytF4oluGF67xJY99pieSnKWt19cbz1vnfDQGZAdqlh4QzTzRfP7uzxUmkxdhfTg4GlZCZBEzZBaT9sJej4dJZCnhtN53BmlCtfabgu7eU3Sapqxtmj2KZC01kkb9cpf",'
                '"categories": ["Sports", "Entertainment", "Technology", "World", "Bangladesh", "Science", "Economy", "City News", "TechStartup", "Islam", "National", "Politics", "Business", "Health"]''}'
            ']'
        }

        response = Facebook.request_to_post_gemten(data)
        return response
    
    def post_to_Gemten_ShowBiz_page(news_id):
        from Helper.helpers import Helper
        template_id = Helper.get_random_one_page_template_id(constants.GEMTEN_ShowBiz_PAGE_ID)
        data = {
            'id': news_id, # News Id
            'template_id': template_id, # Template Id
            'storedPages': '['
                '{"pageId": "680263785168283",'
                '"accessToken": "EAA7ctFADgFIBO1fvbeYTnYZAVVJ480xLQESj5tf0XPbCZCoZA4BrCNifZB9ORsM4ZCw3EZBUZB8WViTZBZCtFoO4cAQM0w1HHqXKP4lEDI9J7BQNTsxFUmyfVf9xCc84PI7rnxYppMGZCmWb2dvj4NCSZA0NkZCGssZBG26PrGKhMZA4DhHxPutuHk1pZCD8ZCEIMxtUORNZBsUek4eeNStx0FFe6uCH9",'
                '"categories": ["Sports", "Entertainment", "Technology", "World", "Bangladesh", "Science", "Economy", "City News", "TechStartup", "Islam", "National", "Politics", "Business", "Health"]''}'
            ']'
        }

        response = Facebook.request_to_post_gemten(data)
        return response
    
    

# https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Faccounts%3Faccess_token%3DLONG_LIVED_USER_TOKEN&version=v22.0

