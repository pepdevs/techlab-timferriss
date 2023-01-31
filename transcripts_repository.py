import pyodbc

def save_episode(showId, episodeNumber, title):
    insertEpisodeCmd = f'''
                            INSERT INTO [dbo].[Episode] 
                                ([EpisodeNumber]
                                ,[ShowId]
                                ,[Title]
                                ,[Date]
                                ,[Length])
                            VALUES
                                ({episodeNumber}
                                ,{showId}
                                ,'{title}'
                                ,NULL
                                ,NULL)
                        '''
    execute_sql_cmd(insertEpisodeCmd)
    return execute_sql_scalar('select IDENT_CURRENT(\'Episode\')')

def save_episode_talk(episodeId, interventionNumber, speaker, speech):
    insertEpisodeTalkCmd = f'''
                                INSERT INTO [dbo].[EpisodeTalk]
                                    ([EpisodeId]
                                    ,[InterventionNumber]
                                    ,[Speaker]
                                    ,[Speech])
                                VALUES
                                    (?,?,?,?)
                            '''
    execute_sql_cmd(insertEpisodeTalkCmd, [episodeId, interventionNumber, speaker, speech])

def clean_show_data(showId):
    execute_sql_cmd(f'DELETE FROM [dbo].[Episode] WHERE ShowId = {showId}')
    execute_sql_cmd(f'''
                        DELETE FROM [dbo].[EpisodeTalk] 
                         WHERE EpisodeId in 
                            (SELECT Id FROM [dbo].[Episode] 
                              WHERE ShowId = {showId})
                     ''')

def get_connection():
    conn = pyodbc.connect('''DRIVER={ODBC Driver 18 for SQL Server};
                          SERVER=localhost;
                          DATABASE=Transcripts;
                          IntegratedSecurity=SSPI;
                          Trusted_Connection=yes;
                          Encrypt=no''')
    return conn

def execute_sql_cmd(cmd, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    if params is None:
        cursor.execute(cmd)
    else:
        cursor.execute(cmd, params)
    cursor.commit()

def execute_sql_scalar(cmd):
    conn = get_connection()
    cursor = conn.cursor()
    scalarValue = cursor.execute(cmd).fetchval()
    return scalarValue
    