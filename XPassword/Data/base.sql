USE [XPassword]
GO
/****** Object:  Table [dbo].[auth]    Script Date: 24.04.2022 21:43:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth](
	[password] [nvarchar](50) NOT NULL,
	[отвеннавопрос1] [nvarchar](50) NOT NULL,
	[отвеннавопрос2] [nvarchar](50) NOT NULL,
	[отвеннавопрос3] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[группы]    Script Date: 24.04.2022 21:43:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[группы](
	[идгруппы] [int] IDENTITY(1,1) NOT NULL,
	[наименование] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[идгруппы] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[запись]    Script Date: 24.04.2022 21:43:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[запись](
	[идзаписи] [int] IDENTITY(1,1) NOT NULL,
	[идсортиовки] [int] NOT NULL,
	[идполя] [int] NOT NULL,
	[идкарты] [int] NOT NULL,
	[Название] [varchar](100) NOT NULL,
	[содержание] [varchar](100) NOT NULL,
 CONSTRAINT [PK__запись__27ABDB28DF01222E] PRIMARY KEY CLUSTERED 
(
	[идзаписи] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[картотека]    Script Date: 24.04.2022 21:43:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[картотека](
	[идкарты] [int] IDENTITY(1,1) NOT NULL,
	[наименование] [varchar](50) NOT NULL,
	[идгруппы] [int] NOT NULL,
 CONSTRAINT [PK__картотек__9976017F7AE73D4D] PRIMARY KEY CLUSTERED 
(
	[идкарты] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[типыполей]    Script Date: 24.04.2022 21:43:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[типыполей](
	[идполя] [int] IDENTITY(1,1) NOT NULL,
	[наименование] [varchar](10) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[идполя] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[auth] ([password], [отвеннавопрос1], [отвеннавопрос2], [отвеннавопрос3]) VALUES (N'admin', N'apple', N'green', N'blue')
GO
SET IDENTITY_INSERT [dbo].[группы] ON 

INSERT [dbo].[группы] ([идгруппы], [наименование]) VALUES (1, N'Соцсети')
INSERT [dbo].[группы] ([идгруппы], [наименование]) VALUES (2, N'Почта')
INSERT [dbo].[группы] ([идгруппы], [наименование]) VALUES (15, N'Работа')
SET IDENTITY_INSERT [dbo].[группы] OFF
GO
SET IDENTITY_INSERT [dbo].[запись] ON 

INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (1, 1, 1, 1, N'Логин', N'asd@mail.ru')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (2, 2, 2, 1, N'Пароль', N'sdsdfSAd231')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (3, 3, 3, 1, N'Сайт', N'vk.ru')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (5, 1, 1, 2, N'Логин', N'asd@asd.com')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (6, 3, 2, 2, N'Пароль', N'123fsdsf')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (7, 2, 3, 2, N'Сайт', N'mail.ru')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (50, 1, 1, 22, N'Логин', N'')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (51, 2, 2, 22, N'Пароль', N'')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (52, 3, 3, 22, N'Сайт', N'')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (53, 1, 1, 23, N'Логин', N'')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (54, 2, 2, 23, N'Пароль', N'')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (55, 3, 3, 23, N'Сайт', N'')
SET IDENTITY_INSERT [dbo].[запись] OFF
GO
SET IDENTITY_INSERT [dbo].[картотека] ON 

INSERT [dbo].[картотека] ([идкарты], [наименование], [идгруппы]) VALUES (1, N'VK', 1)
INSERT [dbo].[картотека] ([идкарты], [наименование], [идгруппы]) VALUES (2, N'Однокласники', 1)
INSERT [dbo].[картотека] ([идкарты], [наименование], [идгруппы]) VALUES (22, N'Gmail', 2)
INSERT [dbo].[картотека] ([идкарты], [наименование], [идгруппы]) VALUES (23, N'Mail', 15)
SET IDENTITY_INSERT [dbo].[картотека] OFF
GO
SET IDENTITY_INSERT [dbo].[типыполей] ON 

INSERT [dbo].[типыполей] ([идполя], [наименование]) VALUES (1, N'логин')
INSERT [dbo].[типыполей] ([идполя], [наименование]) VALUES (2, N'пароль')
INSERT [dbo].[типыполей] ([идполя], [наименование]) VALUES (3, N'сайт')
SET IDENTITY_INSERT [dbo].[типыполей] OFF
GO
ALTER TABLE [dbo].[запись]  WITH CHECK ADD  CONSTRAINT [FK__запись__идкарты__34C8D9D1] FOREIGN KEY([идкарты])
REFERENCES [dbo].[картотека] ([идкарты])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[запись] CHECK CONSTRAINT [FK__запись__идкарты__34C8D9D1]
GO
ALTER TABLE [dbo].[запись]  WITH CHECK ADD  CONSTRAINT [FK__запись__идполя__35BCFE0A] FOREIGN KEY([идполя])
REFERENCES [dbo].[типыполей] ([идполя])
GO
ALTER TABLE [dbo].[запись] CHECK CONSTRAINT [FK__запись__идполя__35BCFE0A]
GO
ALTER TABLE [dbo].[картотека]  WITH CHECK ADD  CONSTRAINT [FK_картотека_группы] FOREIGN KEY([идгруппы])
REFERENCES [dbo].[группы] ([идгруппы])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[картотека] CHECK CONSTRAINT [FK_картотека_группы]
GO
