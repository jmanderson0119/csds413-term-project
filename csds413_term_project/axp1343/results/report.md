# Report ideas

- how we can do classification on complex data using a rather simple model
- the features are easy to calculate


- my tasks: add new features if possible
perform classification using neural network


- I performed classification using multiple algorithms
	•	Cleaned data
	•	Removed extreme outliers
	•	Tried several classifiers (LR, SVM, RF, maybe MLP)
	•	Tuned basic hyperparams

the classes were heavily overlapping




updated analysis, before outlier detection:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>feature</th>
      <th>mean_human</th>
      <th>mean_bot</th>
      <th>mean_diff (bot - human)</th>
      <th>CI_low</th>
      <th>CI_high</th>
      <th>Cohen_d</th>
      <th>t_stat</th>
      <th>df_Welch</th>
      <th>p_value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>V</td>
      <td>0.942439</td>
      <td>0.914278</td>
      <td>-0.028161</td>
      <td>-0.030863</td>
      <td>-0.025459</td>
      <td>-0.270609</td>
      <td>-20.430890</td>
      <td>21540.634577</td>
      <td>6.606341e-92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>S</td>
      <td>11.132062</td>
      <td>13.724572</td>
      <td>2.592510</td>
      <td>2.354925</td>
      <td>2.830095</td>
      <td>0.283331</td>
      <td>21.388196</td>
      <td>21411.596238</td>
      <td>1.934617e-100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>W</td>
      <td>4.411293</td>
      <td>4.129526</td>
      <td>-0.281767</td>
      <td>-0.308345</td>
      <td>-0.255188</td>
      <td>-0.273038</td>
      <td>-20.779474</td>
      <td>19546.671667</td>
      <td>7.036822e-95</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>0.419101</td>
      <td>0.481089</td>
      <td>0.061988</td>
      <td>0.057575</td>
      <td>0.066401</td>
      <td>0.362963</td>
      <td>27.531912</td>
      <td>22506.130740</td>
      <td>3.809901e-164</td>
    </tr>
    <tr>
      <th>4</th>
      <td>C</td>
      <td>0.129610</td>
      <td>0.092857</td>
      <td>-0.036754</td>
      <td>-0.041545</td>
      <td>-0.031962</td>
      <td>-0.197487</td>
      <td>-15.035201</td>
      <td>19113.198714</td>
      <td>8.429145e-51</td>
    </tr>
  </tbody>
</table>
</div>


after removing outliers:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>feature</th>
      <th>mean_human</th>
      <th>mean_bot</th>
      <th>mean_diff (bot - human)</th>
      <th>CI_low</th>
      <th>CI_high</th>
      <th>Cohen_d</th>
      <th>t_stat</th>
      <th>df_Welch</th>
      <th>p_value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>V</td>
      <td>0.943914</td>
      <td>0.918373</td>
      <td>-0.025541</td>
      <td>-0.027924</td>
      <td>-0.023158</td>
      <td>-0.281659</td>
      <td>-21.010767</td>
      <td>20249.883391</td>
      <td>5.662268e-97</td>
    </tr>
    <tr>
      <th>1</th>
      <td>S</td>
      <td>11.538829</td>
      <td>13.771874</td>
      <td>2.233045</td>
      <td>1.995447</td>
      <td>2.470644</td>
      <td>0.247067</td>
      <td>18.421596</td>
      <td>20831.097631</td>
      <td>3.488170e-75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>W</td>
      <td>4.348005</td>
      <td>4.126324</td>
      <td>-0.221681</td>
      <td>-0.242323</td>
      <td>-0.201038</td>
      <td>-0.283321</td>
      <td>-21.049493</td>
      <td>21554.530499</td>
      <td>2.207173e-97</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>0.433097</td>
      <td>0.483502</td>
      <td>0.050405</td>
      <td>0.046210</td>
      <td>0.054600</td>
      <td>0.316805</td>
      <td>23.550993</td>
      <td>21931.618805</td>
      <td>3.906452e-121</td>
    </tr>
    <tr>
      <th>4</th>
      <td>C</td>
      <td>0.087598</td>
      <td>0.087438</td>
      <td>-0.000160</td>
      <td>-0.003282</td>
      <td>0.002962</td>
      <td>-0.001351</td>
      <td>-0.100449</td>
      <td>22051.359469</td>
      <td>9.199888e-01</td>
    </tr>
  </tbody>
</table>
</div>