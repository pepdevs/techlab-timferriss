import pyodbc

def save_episode(episodeNumber, title):
    insertEpisodeCmd = f'''INSERT INTO [dbo].[Episode] 
                                ([EpisodeNumber]
                                ,[ShowId]
                                ,[Title]
                                ,[Date]
                                ,[Length])
                            VALUES
                                ({episodeNumber}
                                ,1
                                ,'{title}'
                                ,NULL
                                ,NULL)'''
    execute_sql_cmd(insertEpisodeCmd)

def execute_sql_cmd(cmd):
    conn = pyodbc.connect('''DRIVER={ODBC Driver 18 for SQL Server};
                          SERVER=localhost;
                          DATABASE=Transcripts;
                          IntegratedSecurity=SSPI;
                          Trusted_Connection=yes;
                          Encrypt=no''')
    cursor = conn.cursor()
    cursor.execute(cmd)
    cursor.commit()
    