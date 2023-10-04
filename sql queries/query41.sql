/*How many items do we carry with specific combinations of color, units, size and category. Qualification Substitution Parameters
 MANUFACT.01 = 738
 SIZE.01 = medium
 SIZE.02 = extra large
 SIZE.03 = N/A
 SIZE.04 = small
 SIZE.05 = petite
 SIZE.06 = large
 UNIT.01 = Ounce
 UNIT.02 = Oz
 UNIT.03 = Bunch
 UNIT.04 = Ton
 UNIT.05 = N/A
 UNIT.06 = Dozen
 UNIT.07 = Box
 UNIT.08 = Pound
 UNIT.09 = Pallet
 UNIT.10 = Gross
 UNIT.11 = Cup
 UNIT.12 = Dram
 UNIT.13 = Each
 UNIT.14 = Tbl
 UNIT.15 = Lb
 UNIT.16 = Bundle
 COLOR.01 = powder
 COLOR.02 = khaki
 COLOR.03 = brown
 COLOR.04 = honeydew
 COLOR.05 = floral
 COLOR.06 = deep
 COLOR.07 = light
 COLOR.08 = cornflower
 COLOR.09 = midnight
 COLOR.10 = snow
 COLOR.11 = cyan
 COLOR.12 = papaya
 COLOR.13 = orange
 COLOR.14 = frosted
 COLOR.15 = forest
 COLOR.16 = ghost
 */

SELECT
    DISTINCT(i_product_name) AS product_name, i_size,
    (
        SELECT COUNT(*) AS item_cnt
        FROM item
        WHERE
            i_manufact = i1.i_manufact
            AND i_size IN ('medium', 'extra large', 'N/A', 'small', 'petite', 'large')
            AND i_units IN ('Ounce', 'OZ', 'Bunch', 'Ton', 'N/A', 'Dozen', 'Box', 'Pound', 'Pallet', 'Gross', 'Cup', 'Dram', 'Each', 'Tbl', 'Lb', 'Bundle')
            AND i_color IN ('powder', 'khaki', 'brown', 'honeydew', 'floral', 'deep', 'light', 'cornflower', 'midnight', 'snow', 'cyan', 'papaya', 'orange', 'frosted', 'forest', 'ghost')
    ) AS item_count
FROM
    item i1
WHERE
    i_manufact_id = 738
ORDER BY
    product_name
LIMIT 100;
