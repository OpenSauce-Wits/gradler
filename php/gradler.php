<?php
// $abs_dir="/home/molefe/Software/Developer/AttributeChangeProject";
define("ABS_DIR","/home/molefe/Software/Developer/AttributeChangeProject");
define("GRADLE_STATUS","gradle_status.txt");
define("GRADLE_FILE","gradle_results.json");
define("SUCCESS_REQUEST_CODE",1);

echo ABS_DIR."<br>";
function getProjectName(){
  $explode = explode("/",ABS_DIR);
  $explode_size = count($explode);
  return $explode[$explode_size-1];
}
$project_name = getProjectName();



function cleanGradler(){
  $clean_output = shell_exec("./reset.sh");
  echo "Cleaning Gradler ....<br>";
  echo $clean_output."<br>";
}
function runGradler($project_name){
  echo "Running Gradler...."."<br>";
  $output = shell_exec("./gradler.sh $project_name ".ABS_DIR);
}


function fetch_gradle_results($project_name){
  cleanGradler();
  runGradler($project_name);

  $gradle_file = fopen(GRADLE_STATUS,"r") or die("Unable To Open File");
  $value = fgets($gradle_file);
  fclose($gradle_file);

  $gradle_json = '{}';
  if(SUCCESS_REQUEST_CODE == $value){
    $gradle_json = file_get_contents(GRADLE_FILE);
    $gradle_decode = json_decode($gradle_json,true);
  }else{
    shell_exec("./reset.sh");
    echo "Please Make Sure That Your Directory Is Correct";
  }

  return $gradle_json;
}

$gradle = fetch_gradle_results($project_name);
echo "<br><br><br>";
echo "The Gradler"."<br>";
echo $gradle;


 ?>
