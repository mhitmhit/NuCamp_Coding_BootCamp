SELECT * FROM moma_artists LIMIT 50;



SELECT jsonb_pretty(info) AS formatted_info
FROM moma_artists LIMIT 50;

SELECT info -> 'display_name' AS name, info -> 'nationality' AS nationality
FROM moma_artists LIMIT 50;



SELECT
info -> 'display_name' AS name,
info -> 'nationality' AS nationality
FROM moma_artists
WHERE info ->> 'nationality' = 'American'
ORDER BY id
LIMIT 50;

-- 3 below serve same purpose:
INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, Ablade Glover, nationality, Ghanaian}')
);

INSERT INTO moma_artists (info) VALUES (
    json_object('{{display_name, Ablade Glover}, {nationality, Ghanaian}}')
);

INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, nationality}', '{Ablade Glover, Ghanaian}')
);
