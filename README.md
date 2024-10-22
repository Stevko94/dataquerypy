# dataquerypy

-- Insert data scripts for testing the database

-- Insert users\INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');

-- Insert posts
INSERT INTO posts (title, content, status, user_id) VALUES
('First Post', 'Content of the first post', 'published', 1),
('Second Post', 'Content of the second post', 'draft', 2),
('Third Post', 'Content of the third post', 'published', 3);

-- Insert comments
INSERT INTO comments (content, user_id, post_id) VALUES
('Great post!', 2, 1),
('Thanks for sharing', 3, 1),
('Interesting read', 1, 3);

-- Insert tags
INSERT INTO tags (name) VALUES
('FastAPI'),
('SQLAlchemy'),
('Python');

-- Insert post_tags relationships
INSERT INTO post_tags (post_id, tag_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 1),
(3, 3);
