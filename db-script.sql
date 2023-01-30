CREATE TABLE Show (
	Id INT NOT NULL IDENTITY PRIMARY KEY,
	Name VARCHAR(255)
)

CREATE TABLE Episode (
	Id INT NOT NULL IDENTITY PRIMARY KEY,
	EpisodeNumber INT,
	ShowId INT,
	Title VARCHAR(255),
	Date DATE,
	Length INT
)

CREATE TABLE EpisodeGuest (
	Id INT NOT NULL IDENTITY PRIMARY KEY,
	EpisodeId INT,
	GuestName VARCHAR(255)
)

CREATE TABLE EpisodeTalk (
	Id INT NOT NULL IDENTITY PRIMARY KEY,
	EpisodeId INT,
	GuestName VARCHAR(255),
	Speech NVARCHAR(max)
)