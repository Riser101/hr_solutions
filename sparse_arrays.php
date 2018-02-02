/*
There is a collection of  N strings ( There can be multiple occurences of a particular string ). Each string's length is no more than 20 characters. There are also Q queries. For each query, you are given a string, and you need to find out how many times this string occurs in the given collection of N strings.

Input Format

The first line contains , N the number of strings.
The next N lines each contain a string.
The N+2nd line contains Q, the number of queries.
The following Q lines each contain a query string.

Constraints
1<= N <= 1000
1<= Q <= 1000
1<= length of any string <= 20

Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output

2
1
0
Explanation

Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string, and "ab" does not occur at all.
*/

<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
    $input_array = array();
    while(!feof($_fp)){
        $line = fgets($_fp);
        array_push($input_array, $line);
    }
    $number_of_strings = $input_array[0];
    $start_index_of_query = $number_of_strings + 2;
    $result_array = array();
    for($i=$start_index_of_query; $i<sizeof($input_array); $i++){
        for($k=1; $k<$start_index_of_query; $k++){
            $result_array[$input_array[$i]]=0;
            if($input_array[$i] === $input_array[$k]){
                for($j=0; $j<=sizeof($result_array); $j++){
                    print_r($result_array);
                    echo($result_array["aba"]);
                    //exit();
                    if($result_array[$j] === $input_array[$i]){
                        
                        exit();
                    }
                }
            }
        }
    }
    //print_r($result_array);                           
?>