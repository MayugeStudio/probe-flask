import mysql.connector
from mysql.connector import Error

def connect_and_query():
    try:
        #　１．DB接続リクエスト
        # MySQLに接続
        connection = mysql.connector.connect(
            host='localhost',  # ホスト名（例: '127.0.0.1'）
            user='root',       # ユーザー名
            password='root',   # パスワード
            database='py12db'  # データベース名
        )
        
        #DB接続が確立しているかをチェック
        if connection.is_connected():
            print("接続成功")

            #接続成功！
            #　２．カーソル生成
            cursor = connection.cursor()

            #　３．SQL発行（実行）
            query = "SELECT * FROM t_user"
            cursor.execute(query)

            #　４．DBレスポンス(データ)受信
            result = cursor.fetchall()
            for row in result:
                print(row)
                for e in row:
                    print(e)

            #　６．カーソル閉じる
            cursor.close()

            #　７．DB接続閉じる
            connection.close()

        
        #結果の表示(1レコードずつ表示)
        print("########################################################")
        print("DBデータ取得結果")
        print("########################################################")


    except Error as e:
        print(f"❌ エラー発生: {e}")

    #finally:


if __name__ == "__main__":
    connect_and_query()
