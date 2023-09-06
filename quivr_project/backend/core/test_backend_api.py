import os
import logger
import requests
from dotenv import load_dotenv


load_dotenv()
logger = logger.get_logger(__name__)

ENDPOINT = "http://walletgpt.info:5050"

########## BRAIN ##########
# Retrieve all brains for the current user.
def test_get_brains(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url=ENDPOINT+'/brains/', headers=headers)
    logger.info('test_get_brains')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")

# Create new brain
def test_post_brains(token, create_brain_data):
    headers = {'Authorization': f'Bearer {token}', "Content-Type": "application/json"}
    response = requests.post(ENDPOINT + '/brains/', json=create_brain_data, headers=headers)

    logger.info('test_post_brains')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")

# Retrieve Brain with ID
def test_retrieve_brain(token, brain_id):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(
        url=ENDPOINT+f'/brains/{brain_id}/',
        headers=headers,
    )

    logger.info('test_chat')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")

########## UPLOAD ##########
# Upload knowledge
def test_post_upload(token, brain_id, file_path):
    headers = {'Authorization': f'Bearer {token}'}  # "Content-Type": "multipart/form-data"
    params = {'brain_id': brain_id}
    
    assert os.path.exists(file_path)
    with open(file_path, 'rb') as f:
        files = {
            'uploadFile': f  # creates a FileStorage object with the file's content and filename.
        }
        response = requests.post(ENDPOINT+'/upload', params=params, headers=headers, files=files)
        
        logger.info('test_post_brains')
        logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")

########## CRAWL ##########
# LinkedIn 
def test_linkedin_scraping(token, brain_id):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'brain_id': brain_id}
    response = requests.post(ENDPOINT+'/crawl/linkedin', params=params, headers=headers)

    logger.info('test_linkedin_scraping')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")

########## EXPLORER ##########
# Get all data
def test_get_data(token, brain_id):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'brain_id': brain_id}
    response = requests.get(ENDPOINT+f'/explore/', params=params, headers=headers)
    logger.info('test_get_data')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")

# Delete data
def test_delete_data(token, brain_id, data_sha1):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'brain_id': brain_id}
    response = requests.delete(ENDPOINT+f'/explore/data/{data_sha1}/', params=params, headers=headers)
    logger.info('test_delete_data')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")


########## CHAT ##########
# Chat with Brain
def test_post_chat(token, chat_id, brain_id, question):
    headers = {'Authorization': f'Bearer {token}',  "Content-Type": "application/json"}
    params = {'brain_id': brain_id}
    data = {'question': question}

    response = requests.post(
        url=ENDPOINT+f'/chat/{chat_id}/question/stream', 
        headers=headers,
        params=params,
        json=data
    )

    logger.info('test_post_chat')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")

# Choose nearest experts
def test_choose_nearest_experts(token, query:str):
    headers = {'Authorization': f'Bearer {token}',  "Content-Type": "application/json"}
    data = {'question': query}

    response = requests.post(
        url=ENDPOINT+f'/chat/choose', 
        headers=headers,
        json=data
    )

    logger.info('test_choose_nearest_experts')
    logger.info(f"status_code: {response.status_code}, \ttext: {response.text}")


if __name__ == "__main__":
    create_brain_data = {
        'description': "unittest",
        'name': 'unittest brain',
        'model': 'gpt-3.5-turbo-0613',
        'max_tokens': 378,
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'temperature': '0.75',
        'prompt_id': None,
        'linkedin': None,
        'extraversion': 3,
        'neuroticism': 0,
        'conscientiousness': 3
    }

    brain_id = 'b8d1e86b-7e22-4c9f-96d2-14f01bf5d1d3'
    file_path = '/root/hongyu/customersupportgpt/quivr_project/backend/core/unittest-upload.txt'
    chat_id = "6b14af62-608a-4787-b21c-3a48a0352897"
    question = "How about your personality?"

    hongyu_token = "091113066d5725238656d784c71c2f22"

    ##### Create experts
    # experts = [
    #     {
    #     'name': 'expert1',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 256,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.5',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/samuel-sebban-b09b5a105/",
    #     'extraversion': 2,
    #     'neuroticism': 1,
    #     'conscientiousness': 3
    #     },{
    #     'name': 'expert2',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 350,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.3',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/franckhagege/",
    #     'extraversion': 1,
    #     'neuroticism': 2,
    #     'conscientiousness': 2
    #     },{
    #     'name': 'expert3',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 256,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.4',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/jean-du-boisdulier-4986199b/",
    #     'extraversion': 3,
    #     'neuroticism': 0,
    #     'conscientiousness': 2
    #     },{
    #     'name': 'expert4',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 256,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.6',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/herv%C3%A9-patrick-amon-39b88768/",
    #     'extraversion': 2,
    #     'neuroticism': 0,
    #     'conscientiousness': 0
    #     },{
    #     'name': 'expert5',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 400,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.8',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/antoine-loubaud/",
    #     'extraversion': 0,
    #     'neuroticism': 2,
    #     'conscientiousness': 3
    #     },{
    #     'name': 'expert6',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 300,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.1',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/olivierpate/",
    #     'extraversion': 1,
    #     'neuroticism': 2,
    #     'conscientiousness': 3
    #     },{
    #     'name': 'expert7',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 256,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.7',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/josselin-larriviere-8100b824/",
    #     'extraversion': 3,
    #     'neuroticism': 3,
    #     'conscientiousness': 3
    #     },{
    #     'name': 'expert8',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 512,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.9',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/thibault-lassiaz-07015518/",
    #     'extraversion': 2,
    #     'neuroticism': 2,
    #     'conscientiousness': 1
    #     },{
    #     'name': 'expert9',
    #     'description': "investment advisor",
    #     'model': 'gpt-3.5-turbo-0613',
    #     'max_tokens': 378,
    #     'openai_api_key': os.getenv('OPENAI_API_KEY'),
    #     'temperature': '0.2',
    #     'prompt_id': None,
    #     'linkedin': "https://www.linkedin.com/in/hugo-derny-055b262b/",
    #     'extraversion': 2,
    #     'neuroticism': 0,
    #     'conscientiousness': 0
    #     }
    # ]
    
    # for expert in experts:
    #     test_post_brains(hongyu_token, expert)


    # test_post_brains(hongyu_token, andrew_data)
    # test_post_brains(hongyu_token, jeffBezos_data)
    
    ##### Get All brains
    # test_get_brains(hongyu_token)

    ##### Linkedin scraping
    brain_ids = [
        "fdcce4d8-fba7-4276-b9f6-53c5e8a3a3b0",
        "ab2fcf67-3651-43ca-9326-fbc964eb7315",
        "725687d5-8b99-45bf-9612-c6cfa3dc7e7b",
        "d129033e-25db-4658-8d3d-d83f333fe974",
        "cde68b32-fc0b-4866-8280-e2efd42a5a11",
        "9be9ad3e-4bcc-4c8e-95f0-fe2286bb40e8",
        "2eae212c-8712-48f5-907d-551e8e57683a",
        "1e87cafa-9f6c-40f5-8d3f-0e8b7ef7488b",
        "2ca5281f-c8e4-44c0-bca0-f2bc23d22660"
    ]
    # for brain_id in brain_ids[:1]:
    #     test_linkedin_scraping(token=hongyu_token, brain_id=brain_id)

    ##### Get all data


    ##### Delete data
    # data_sha1_list = [
    #     "13ccc461bb34d02f78b94d7afe05735e17577732",
    #     "67bbbbdb8ea5bfa4846b3a0864f140d2f5f4be7e",
    #     "a43a0ea4aadcb12417e30543cb1bacba4f12e542"
    # ]
    # for data_sha1 in data_sha1_list:
    #     test_delete_data(hongyu_token, brain_ids[0], data_sha1)

    # for i, brain_id in enumerate(brain_ids):
    test_delete_data(hongyu_token, "fdcce4d8-fba7-4276-b9f6-53c5e8a3a3b0", "76c454cb6f828971fd3168a0d4cc0445e7cababe")
    # test_delete_data(hongyu_token, "fdcce4d8-fba7-4276-b9f6-53c5e8a3a3b0", "7a1bec116ac29b982b71b4312fdbd717634c3a95")

    ##### Choose nearest experts
    # test_choose_nearest_experts(hongyu_token, query="hello world!")

    # andrew_brain_id = "7b78d424-4d17-4ef1-bcea-f28de168c5d9"
    # jeff_brain_id = "18c768d5-6096-447a-b5e5-0f8a267bc09a"

    # test_linkedin_scraping(token=hongyu_token, brain_id=andrew_brain_id)

    # test_delete_data(token=hongyu_token, brain_id=andrew_brain_id, data_sha1='5908b0137643d9f431bcc0848e7dea4fdc33d905')