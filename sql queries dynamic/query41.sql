

SELECT
    DISTINCT(i_product_name) AS product_name, i_size,
    (
        SELECT COUNT(*) AS item_cnt
        FROM item
        WHERE
            i_manufact = i1.i_manufact
            AND i_size IN {0}
            AND i_units IN {1}
            AND i_color IN {2}
            ) AS item_count
FROM
    item i1
WHERE
    i_manufact_id = 738
ORDER BY
    product_name
LIMIT 100;
