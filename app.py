import streamlit as st
import openai

# 初期設定
openai_api_key = st.secrets['api_key']


# タイトル出力
st.title('おすすめの趣味・職業')


# form設定
with st.form("form"):
    # パスワード入力欄
    input_password = st.text_input('passwordを入力してください')
    # おすすめ内容種類入力欄
    user_topic = st.selectbox('おすすめして欲しい内容を選択してください',('趣味','職業'))
    # 年齢入力欄
    user_age = st.text_input('年齢を記入してください')
    # 好きなこと入力欄
    user_like = st.text_input('好きなことを記入してください（ex.ギター演奏、本を読むこと、旅行）')
    # 部活・習い事などの経験入力欄
    user_experience = st.text_input('部活・習い事など、今まで経験したことを記入してください（ex.サッカー部、飲食業）')

    # 作成ボタン
    submit = st.form_submit_button("作成")


# inputに内容があり、作成ボタンを押した際に出力する
# if submit and user_topic and "cloudseed" == input_password:
if submit and user_topic and "" == input_password:
    with st.spinner('回答を作成中......'):

        # プロンプトの生成
        # prompt = f'''
        # "User Infomation"に基づいて、userにおすすめの{user_topic}を"Response Format"に従って提案してください。

        # # User Infomation
        # *年齢:{user_age}
        # *好きなこと:{user_like}
        # *今まで経験したこと:{user_experience}

        # # Response Format
        # *提案する個数は5つ
        # *マークダウン形式
        # *日本語
        # '''
        prompt = f'''
        私は{user_like}が好きで、{user_experience}などを経験したことがあるのですが、私におすすめな{user_topic}はありますか？

        # Response Format
        *提案する個数は5つ
        *回答はマークダウン形式
        *回答は日本語
        '''

        # APIアクセス
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                # {"role": "system", "content": "あなたはuserの相談にのるuserの友人です。userの相談に対して日本語かつマークダウン形式で回答してください。"},
                {"role": "user", "content": user_topic}
            ]
        )

    prompt = response["choices"][0]["message"]["content"]
    st.write(prompt)