USE [XPassword]
GO
/****** Object:  Table [dbo].[группы]    Script Date: 04.04.2022 13:57:03 ******/
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
/****** Object:  Table [dbo].[запись]    Script Date: 04.04.2022 13:57:03 ******/
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
/****** Object:  Table [dbo].[картотека]    Script Date: 04.04.2022 13:57:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[картотека](
	[идкарты] [int] IDENTITY(1,1) NOT NULL,
	[наименование] [varchar](50) NOT NULL,
 CONSTRAINT [PK__картотек__9976017F7AE73D4D] PRIMARY KEY CLUSTERED 
(
	[идкарты] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[сплитгруппыкартотеки]    Script Date: 04.04.2022 13:57:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[сплитгруппыкартотеки](
	[идсплит] [int] IDENTITY(1,1) NOT NULL,
	[идкарты] [int] NOT NULL,
	[идгруппы] [int] NOT NULL,
 CONSTRAINT [PK_сплитгруппыкартотеки] PRIMARY KEY CLUSTERED 
(
	[идсплит] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[типыполей]    Script Date: 04.04.2022 13:57:03 ******/
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
SET IDENTITY_INSERT [dbo].[группы] ON 

INSERT [dbo].[группы] ([идгруппы], [наименование]) VALUES (1, N'соцсети')
INSERT [dbo].[группы] ([идгруппы], [наименование]) VALUES (2, N'почта')
INSERT [dbo].[группы] ([идгруппы], [наименование]) VALUES (3, N'работа')
SET IDENTITY_INSERT [dbo].[группы] OFF
GO
SET IDENTITY_INSERT [dbo].[запись] ON 

INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (1, 1, 1, 1, N'Логин', N'asd@mail.ru')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (2, 2, 2, 1, N'Пароль', N'sdsdfSAd231')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (3, 3, 3, 1, N'Сайт', N'vk.ru')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (5, 1, 1, 2, N'Логин', N'asd@asd.com')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (6, 3, 2, 2, N'Пароль', N'123fsdsf')
INSERT [dbo].[запись] ([идзаписи], [идсортиовки], [идполя], [идкарты], [Название], [содержание]) VALUES (7, 2, 3, 2, N'Сайт', N'mail.ru')
SET IDENTITY_INSERT [dbo].[запись] OFF
GO
SET IDENTITY_INSERT [dbo].[картотека] ON 

INSERT [dbo].[картотека] ([идкарты], [наименование]) VALUES (1, N'vk')
INSERT [dbo].[картотека] ([идкарты], [наименование]) VALUES (2, N'однокласники')
INSERT [dbo].[картотека] ([идкарты], [наименование]) VALUES (3, N'mail')
INSERT [dbo].[картотека] ([идкарты], [наименование]) VALUES (5, N'gmail')
SET IDENTITY_INSERT [dbo].[картотека] OFF
GO
SET IDENTITY_INSERT [dbo].[сплитгруппыкартотеки] ON 

INSERT [dbo].[сплитгруппыкартотеки] ([идсплит], [идкарты], [идгруппы]) VALUES (1, 1, 1)
INSERT [dbo].[сплитгруппыкартотеки] ([идсплит], [идкарты], [идгруппы]) VALUES (2, 2, 1)
INSERT [dbo].[сплитгруппыкартотеки] ([идсплит], [идкарты], [идгруппы]) VALUES (3, 3, 2)
INSERT [dbo].[сплитгруппыкартотеки] ([идсплит], [идкарты], [идгруппы]) VALUES (4, 5, 2)
INSERT [dbo].[сплитгруппыкартотеки] ([идсплит], [идкарты], [идгруппы]) VALUES (5, 3, 3)
INSERT [dbo].[сплитгруппыкартотеки] ([идсплит], [идкарты], [идгруппы]) VALUES (6, 5, 3)
SET IDENTITY_INSERT [dbo].[сплитгруппыкартотеки] OFF
GO
SET IDENTITY_INSERT [dbo].[типыполей] ON 

INSERT [dbo].[типыполей] ([идполя], [наименование]) VALUES (1, N'логин')
INSERT [dbo].[типыполей] ([идполя], [наименование]) VALUES (2, N'пароль')
INSERT [dbo].[типыполей] ([идполя], [наименование]) VALUES (3, N'сайт')
SET IDENTITY_INSERT [dbo].[типыполей] OFF
GO
ALTER TABLE [dbo].[запись]  WITH CHECK ADD  CONSTRAINT [FK__запись__идкарты__34C8D9D1] FOREIGN KEY([идкарты])
REFERENCES [dbo].[картотека] ([идкарты])
GO
ALTER TABLE [dbo].[запись] CHECK CONSTRAINT [FK__запись__идкарты__34C8D9D1]
GO
ALTER TABLE [dbo].[запись]  WITH CHECK ADD  CONSTRAINT [FK__запись__идполя__35BCFE0A] FOREIGN KEY([идполя])
REFERENCES [dbo].[типыполей] ([идполя])
GO
ALTER TABLE [dbo].[запись] CHECK CONSTRAINT [FK__запись__идполя__35BCFE0A]
GO
ALTER TABLE [dbo].[сплитгруппыкартотеки]  WITH CHECK ADD  CONSTRAINT [FK_сплитгруппыкартотеки_группы] FOREIGN KEY([идгруппы])
REFERENCES [dbo].[группы] ([идгруппы])
GO
ALTER TABLE [dbo].[сплитгруппыкартотеки] CHECK CONSTRAINT [FK_сплитгруппыкартотеки_группы]
GO
ALTER TABLE [dbo].[сплитгруппыкартотеки]  WITH CHECK ADD  CONSTRAINT [FK_сплитгруппыкартотеки_картотека] FOREIGN KEY([идкарты])
REFERENCES [dbo].[картотека] ([идкарты])
GO
ALTER TABLE [dbo].[сплитгруппыкартотеки] CHECK CONSTRAINT [FK_сплитгруппыкартотеки_картотека]
GO
