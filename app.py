import subprocess
from subprocess import PIPE, STDOUT
from flask import Flask, render_template, request, jsonify

QUESTION_DIR = "question/01/"


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="./static")

    @app.route("/", methods=["GET"])
    def root():
        question_txt = load_question_txt()
        return render_template("index.html", question_txt=question_txt)

    @app.route("/exec", methods=["POST"])
    def exec():
        # フロントエンドから送られてきたtextデータを取得
        text = request.form.get("text")
        # 期待する出力を読み込み
        with open(f"{QUESTION_DIR}expected_output.txt", "r") as f:
            expected_output = f.readline()
            print(expected_output)
        # 入力されたtextデータを評価
        result = is_correct(expected_output, text)
        return jsonify({"result": result})

    def save_file(text: str) -> None:
        file_name = "temp.py"
        with open(file_name, "w") as f:
            f.write(text)

    def exec_file() -> str:
        cmd = f"python3 tmp.py < {QUESTION_DIR}input.txt"
        result = subprocess.run(cmd, stdout=PIPE, stderr=STDOUT, shell=True, text=True)
        return result.stdout

    def is_correct(expected_output, input_text) -> bool:
        save_file(text=input_text)
        answer_output = exec_file()
        return expected_output == answer_output

    def load_question_txt() -> list:
        with open(f"{QUESTION_DIR}question.txt", "r") as f:
            question_txt = f.readlines()
        return question_txt

    return app
