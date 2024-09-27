-- Populates the database with sample data for testing purposes.
-- This script should be run after the PlayNexus database has been created.
-- Requires a MySQL database server to run.

USE PlayNexus;

-- Poplate the Account table with sample data.
INSERT INTO Account (email, password, type) VALUES
    ('lucas.martins@email.com', 'Senha@1234', 'Gamer'),
    ('sofia.ribeiro@gmail.com', 'MeuSenha@2024', 'Gamer'),
    ('renan.souza@outlook.com', 'SenhaSegura!789', 'Gamer'),
    ('clara.santos@yahoo.com', 'Clara1234!', 'Gamer'),
    ('felipe.lima@live.com', 'Felipe!2024', 'Gamer'),
    ('ana.pereira@ea.com', 'Ana@Senha2024', 'Publisher'),
    ('joao.almeida@ubsoft.com', 'Joao1234!', 'Publisher'),
    ('julia.ferreira@activision.com', 'Julia@Senha88', 'Publisher'),
    ('tiago.melo@bethesda.com', 'Tiago!Senha2024', 'Publisher'),
    ('isabela.silva@take-two.com', 'Isabela@Senha1', 'Publisher');

-- Populate the Gamer table with sample data:
INSERT INTO Gamer VALUES
    ('lucas.martins@email.com', 'lucas.martins', '1990-05-12', 'Brasil', NULL),
    ('sofia.ribeiro@gmail.com', 'sofia.ribeiro', '1992-11-23', 'Portugal', NULL),
    ('renan.souza@outlook.com', 'renan.souza', '1989-08-30', 'Brasil', NULL),
    ('clara.santos@yahoo.com', 'clara.santos', '1994-02-17', 'Angola', NULL),
    ('felipe.lima@live.com', 'felipe.lima', '1982-12-05', 'Brasil', NULL);

-- Populate the Publisher table with sample data:
INSERT INTO Publisher VALUES
    ('ana.pereira@ea.com', 'Electronic Arts'),
    ('joao.almeida@ubsoft.com', 'Ubisoft'),
    ('julia.ferreira@activision.com', 'Activision'),
    ('tiago.melo@bethesda.com', 'Bethesda'),
    ('isabela.silva@take-two.com', 'Take-Two Interactive');

-- Populate the Game table with sample data:
INSERT INTO Game VALUES
    ('FIFA 24', 'ana.pereira@ea.com', 'EA Sports', 'Esporte', '2023-09-29', 'O mais recente jogo da série FIFA, oferecendo uma experiência de futebol realista com gráficos melhorados e novos modos de jogo.', NULL, NULL, NULL, 59.99),
    ('Assassins Creed Mirage', 'joao.almeida@ubsoft.com', 'Ubisoft Bordeaux', 'Ação/Aventura', '2023-10-05', 'Um jogo de ação e aventura ambientado na Bagdá medieval, com foco em furtividade e exploração.', NULL, NULL, NULL, 54.99),
    ('Call of Duty: Modern Warfare II', 'julia.ferreira@activision.com', 'Infinity Ward', 'Tiro em Primeira Pessoa', '2022-10-28', 'A continuação da popular série Modern Warfare, com uma campanha intensa e modos multijogador expansivos.', NULL, NULL, NULL, 69.99),
    ('Starfield', 'tiago.melo@bethesda.com', 'Bethesda Game Studios', 'RPG', '2023-09-06', 'Um RPG espacial de mundo aberto, permitindo aos jogadores explorar uma galáxia vasta e cheia de mistérios.', NULL, NULL, NULL, 69.99),
    ('Grand Theft Auto VI', 'isabela.silva@take-two.com', 'Rockstar Games', 'Ação/Aventura', '2024-03-05', 'O aguardado próximo título da série GTA, prometendo uma cidade vibrante e uma narrativa rica com múltiplas opções de jogabilidade.', NULL, NULL, NULL, 74.99),
    ('Madden NFL 24', 'ana.pereira@ea.com', 'EA Tiburon', 'Esporte', '2023-08-15', 'A mais recente entrada na série Madden NFL, com melhorias nas mecânicas de jogo e novas características táticas.', NULL, NULL, NULL, 59.99),
    ('Far Cry 7', 'joao.almeida@ubsoft.com', 'Ubisoft Montreal', 'Ação/Aventura', '2024-02-20', 'Uma nova aventura em um ambiente exótico, repleta de combate, exploração e uma narrativa envolvente.', NULL, NULL, NULL, 64.99),
    ('Diablo IV', 'julia.ferreira@activision.com', 'Blizzard Entertainment', 'RPG de Ação', '2023-06-06', 'O retorno da clássica série Diablo, com uma nova história sombria e uma vasta quantidade de itens e habilidades para explorar.', NULL, NULL, NULL, 69.99),
    ('Elder Scrolls VI', 'tiago.melo@bethesda.com', 'Bethesda Game Studios', 'RPG', '2024-11-15', 'A tão esperada continuação da saga Elder Scrolls, oferecendo um novo mundo rico para explorar e uma narrativa profunda.', NULL, NULL, NULL, 74.99),
    ('Red Dead Redemption 2', 'isabela.silva@take-two.com', 'Rockstar Games', 'Ação/Aventura', '2018-10-26', 'Um épico de faroeste que mergulha os jogadores em um mundo aberto com uma narrativa envolvente e um ambiente imersivo.', NULL, NULL, NULL, 59.99);
