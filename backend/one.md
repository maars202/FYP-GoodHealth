SELECT 
    post.id, post.title, post.content, COMMENT.content, COMMENT.post_id
FROM 
    post
INNER JOIN 
    COMMENT
ON
    post.id=COMMENT.post_id;