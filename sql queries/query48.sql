/*Calculate the total sales by different types of customers 
(e.g., based on marital status, education status), sales price and 
different combinations of state and sales profit. 
Qualification Substitution Parameters:
 MS.1=M
 MS.2=D
 MS.3=S
 ES.1=4 yr Degree
 ES.2=2 yr Degree
 ES.3=College
 STATE.1=CO
 STATE.2=OH
 STATE.3=TX
 STATE.4=OR
 STATE.5=MN
 STATE.6=KY
 STATE.7=VA
 STATE.8=CA
 STATE.9=MS
 YEAR.1=2000 */

SELECT
    SUM(ss_quantity),
    cd_marital_status,
    cd_education_status,
    ca_state
FROM
    store_sales,
    store,
    customer_demographics,
    customer_address,
    date_dim
WHERE
    s_store_sk = ss_store_sk
    AND ss_sold_date_sk = d_date_sk
    AND d_year = 2000
    AND (
        (
            cd_demo_sk = ss_cdemo_sk
            AND cd_marital_status = 'M'
            AND cd_education_status = '4 yr Degree'
        )
        OR (
            cd_demo_sk = ss_cdemo_sk
            AND cd_marital_status = 'D'
            AND cd_education_status = '2 yr Degree'
        )
        OR (
            cd_demo_sk = ss_cdemo_sk
            AND cd_marital_status = 'S'
            AND cd_education_status = 'College'
        )
    )
    AND (
        ss_addr_sk = ca_address_sk
        AND ca_country = 'United States'
        AND ca_state IN ('CO', 'OH', 'TX', 'OR', 'MN', 'KY', 'VA', 'CA', 'MS')
    )
GROUP BY
    cd_marital_status,
    cd_education_status,
    ca_state
LIMIT 100;


