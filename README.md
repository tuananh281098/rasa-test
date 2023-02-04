## How to install
- [Get started with Rasa](https://rasa.com/docs/rasa/user-guide/installation/)
- [Get started with Rasa X](https://rasa.com/docs/rasa-x/installation-and-setup/)
*note: you needn't install RasaX if you dont like
- Rasa-SDK -> pip install rasa-sdk

## Core
- Rasa -> include Rasa NLU and Rasa Core
- Rasa X -> interface to manage data, chat log or teach bot
- Rasa-SDK, using Python to change custom actions

## Where is data?
- data/nlu.md: this is the file which will be trained by Rasa NLU, and it's pattern user message
- data/stories.md: this is timeline the conversations. It match pattern message of users with pattern message of bot
- domain.yml: this is a initialy file (i think so). You will init entities, actions and intents in here

## References: 
 - https://medium.com/@itsromiljain/build-a-conversational-chatbot-with-rasa-stack-and-python-rasa-nlu-b79dfbe59491 -> how to build a rasa chat bot step by step
 - https://github.com/RasaHQ/rasa/pull/1312 -> import file txt to training data


## Build Rasa to server
### 1. Config
- Tải file rsa key (chatbot.pem) và cop vào thư mục `.ssh` (nếu chưa có thì tạo folder này `C:\Users\your_username\.ssh`)
- Tạo file config trong thư mục `/.ssh`
- Edit file config thêm đoạn config sau:
    ~~~
    Host chatbot
    HostName ec2-13-251-78-23.ap-southeast-1.compute.amazonaws.com
    User ubuntu
    IdentityFile "`đường dẫn tới file chatbot.pem`"
    ~~~
### 2. Train model
- Train model ở máy local bằng lệnh `rasa train`
### 3. Build
- Sau khi train, tải model mới nhất lên server bằng lệnh  
`scp -i ~/.ssh/chatbot.pem -r ~/vietnamese-chat-with-rasa/models/`model-name]`.tar.gz ubuntu@13.251.78.23:rasa-voice-chat/models`
- Connect đến server bằng lệnh `ssh chatbot`
- Dùng venv `source voice-chatbot-venv/bin/activate`
- Chuyển đến thư mục `rasa-voice-chat`
- Kill rasa server nếu nó đang chạy `sudo kill -9 $(sudo lsof -t -i:5000)`
- Kill rasa actions nếu nó đang chạy `sudo kill -9 $(sudo lsof -t -i:5055)`
- Restart rasa server `nohup rasa run &`
- Restart rasa actions `nohup rasa run actions &`