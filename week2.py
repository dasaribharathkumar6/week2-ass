{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7e90221d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>session</th>\n",
       "      <th>year</th>\n",
       "      <th>country</th>\n",
       "      <th>country_name</th>\n",
       "      <th>speaker</th>\n",
       "      <th>position</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>ALB</td>\n",
       "      <td>Albania</td>\n",
       "      <td>Mr. NAS</td>\n",
       "      <td>NaN</td>\n",
       "      <td>33: May I first convey to our President the co...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>ARG</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>Mr. DE PABLO PARDO</td>\n",
       "      <td>NaN</td>\n",
       "      <td>177.\\t : It is a fortunate coincidence that pr...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>AUS</td>\n",
       "      <td>Australia</td>\n",
       "      <td>Mr. McMAHON</td>\n",
       "      <td>NaN</td>\n",
       "      <td>100.\\t  It is a pleasure for me to extend to y...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>AUT</td>\n",
       "      <td>Austria</td>\n",
       "      <td>Mr. KIRCHSCHLAEGER</td>\n",
       "      <td>NaN</td>\n",
       "      <td>155.\\t  May I begin by expressing to Ambassado...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>BEL</td>\n",
       "      <td>Belgium</td>\n",
       "      <td>Mr. HARMEL</td>\n",
       "      <td>NaN</td>\n",
       "      <td>176. No doubt each of us, before coming up to ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>BLR</td>\n",
       "      <td>Belarus</td>\n",
       "      <td>Mr. GURINOVICH</td>\n",
       "      <td>NaN</td>\n",
       "      <td>\\n71.\\t. We are today mourning the untimely de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>BOL</td>\n",
       "      <td>Bolivia, Plurinational State of</td>\n",
       "      <td>Mr. CAMACHO OMISTE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135.\\t  I wish to congratulate the President o...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>BRA</td>\n",
       "      <td>Brazil</td>\n",
       "      <td>Mr. GIBSON BARBOZA</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.\\tMr. President, I should like, first of all...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>CAN</td>\n",
       "      <td>Canada</td>\n",
       "      <td>Mr. SHARP</td>\n",
       "      <td>NaN</td>\n",
       "      <td>\\nThe General Assembly is fortunate indeed to ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>CMR</td>\n",
       "      <td>Cameroon</td>\n",
       "      <td>Mr. AHIDJO</td>\n",
       "      <td>President</td>\n",
       "      <td>: A year ago I came here as the Acting Preside...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>COG</td>\n",
       "      <td>Congo</td>\n",
       "      <td>Mr. ICKONGA</td>\n",
       "      <td>NaN</td>\n",
       "      <td>122.\\t  I cannot begin my intervention without...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>COL</td>\n",
       "      <td>Colombia</td>\n",
       "      <td>Mr. VASQUEZ CARRIZOSA</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Mr. President, this visit to the United Nation...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>CRI</td>\n",
       "      <td>Costa Rica</td>\n",
       "      <td>Mr. FACIO</td>\n",
       "      <td>NaN</td>\n",
       "      <td>62.\\t  Mr. President, your election to the Pre...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>CUB</td>\n",
       "      <td>Cuba</td>\n",
       "      <td>Mr. ALARCON</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.\\t  Mr. President, I should first like to co...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>DOM</td>\n",
       "      <td>Dominican Republic</td>\n",
       "      <td>Mr FERNANDEZ G.</td>\n",
       "      <td></td>\n",
       "      <td>\\n\\n\\n Mr. President, it was a source of great...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>DZA</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>Mr. YAZID</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.  The delegation of Algeria is very pleased ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>ECU</td>\n",
       "      <td>Ecuador</td>\n",
       "      <td>Mr. Benites</td>\n",
       "      <td>NaN</td>\n",
       "      <td>71.  It had been my hope that a loftier person...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>FRA</td>\n",
       "      <td>France</td>\n",
       "      <td>Mr. SCHUMANN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>84.\\t  Within one month, when we celebrate the...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>GBR</td>\n",
       "      <td>United Kingdom</td>\n",
       "      <td>Sir Alec DOUGLASHOME</td>\n",
       "      <td>NaN</td>\n",
       "      <td>110.\\t Mr. President, I should like first to s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>25</td>\n",
       "      <td>1970</td>\n",
       "      <td>GHA</td>\n",
       "      <td>Ghana</td>\n",
       "      <td>Mr. OWUSU</td>\n",
       "      <td>NaN</td>\n",
       "      <td>121.\\t I should like to begin by congratulatin...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    session  year country                     country_name  \\\n",
       "0        25  1970     ALB                          Albania   \n",
       "1        25  1970     ARG                        Argentina   \n",
       "2        25  1970     AUS                        Australia   \n",
       "3        25  1970     AUT                          Austria   \n",
       "4        25  1970     BEL                          Belgium   \n",
       "5        25  1970     BLR                          Belarus   \n",
       "6        25  1970     BOL  Bolivia, Plurinational State of   \n",
       "7        25  1970     BRA                           Brazil   \n",
       "8        25  1970     CAN                           Canada   \n",
       "9        25  1970     CMR                         Cameroon   \n",
       "10       25  1970     COG                            Congo   \n",
       "11       25  1970     COL                         Colombia   \n",
       "12       25  1970     CRI                       Costa Rica   \n",
       "13       25  1970     CUB                             Cuba   \n",
       "14       25  1970     DOM               Dominican Republic   \n",
       "15       25  1970     DZA                          Algeria   \n",
       "16       25  1970     ECU                          Ecuador   \n",
       "17       25  1970     FRA                           France   \n",
       "18       25  1970     GBR                   United Kingdom   \n",
       "19       25  1970     GHA                            Ghana   \n",
       "\n",
       "                  speaker    position  \\\n",
       "0                 Mr. NAS         NaN   \n",
       "1      Mr. DE PABLO PARDO         NaN   \n",
       "2             Mr. McMAHON         NaN   \n",
       "3      Mr. KIRCHSCHLAEGER         NaN   \n",
       "4              Mr. HARMEL         NaN   \n",
       "5          Mr. GURINOVICH         NaN   \n",
       "6      Mr. CAMACHO OMISTE         NaN   \n",
       "7      Mr. GIBSON BARBOZA         NaN   \n",
       "8               Mr. SHARP         NaN   \n",
       "9              Mr. AHIDJO  President    \n",
       "10            Mr. ICKONGA         NaN   \n",
       "11  Mr. VASQUEZ CARRIZOSA         NaN   \n",
       "12              Mr. FACIO         NaN   \n",
       "13            Mr. ALARCON         NaN   \n",
       "14        Mr FERNANDEZ G.               \n",
       "15              Mr. YAZID         NaN   \n",
       "16            Mr. Benites         NaN   \n",
       "17           Mr. SCHUMANN         NaN   \n",
       "18   Sir Alec DOUGLASHOME         NaN   \n",
       "19              Mr. OWUSU         NaN   \n",
       "\n",
       "                                                 text  \n",
       "0   33: May I first convey to our President the co...  \n",
       "1   177.\\t : It is a fortunate coincidence that pr...  \n",
       "2   100.\\t  It is a pleasure for me to extend to y...  \n",
       "3   155.\\t  May I begin by expressing to Ambassado...  \n",
       "4   176. No doubt each of us, before coming up to ...  \n",
       "5   \\n71.\\t. We are today mourning the untimely de...  \n",
       "6   135.\\t  I wish to congratulate the President o...  \n",
       "7   1.\\tMr. President, I should like, first of all...  \n",
       "8   \\nThe General Assembly is fortunate indeed to ...  \n",
       "9   : A year ago I came here as the Acting Preside...  \n",
       "10  122.\\t  I cannot begin my intervention without...  \n",
       "11  Mr. President, this visit to the United Nation...  \n",
       "12  62.\\t  Mr. President, your election to the Pre...  \n",
       "13  1.\\t  Mr. President, I should first like to co...  \n",
       "14  \\n\\n\\n Mr. President, it was a source of great...  \n",
       "15  1.  The delegation of Algeria is very pleased ...  \n",
       "16  71.  It had been my hope that a loftier person...  \n",
       "17  84.\\t  Within one month, when we celebrate the...  \n",
       "18  110.\\t Mr. President, I should like first to s...  \n",
       "19  121.\\t I should like to begin by congratulatin...  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "file = \"C:\\\\Users\\\\jyoth\\\\Downloads\\\\un-general-debates-blueprint (1).csv\"\n",
    "df = pd.read_csv(file)\n",
    "df.head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "0ce22494",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.sample(frac=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "6b3fe297",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['session', 'year', 'country', 'country_name', 'speaker', 'position',\n",
       "       'text'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "8ead0134",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "session          int64\n",
       "year             int64\n",
       "country         object\n",
       "country_name    object\n",
       "speaker         object\n",
       "position        object\n",
       "text            object\n",
       "dtype: object"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "79aae418",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 1501 entries, 1370 to 5677\n",
      "Data columns (total 7 columns):\n",
      " #   Column        Non-Null Count  Dtype \n",
      "---  ------        --------------  ----- \n",
      " 0   session       1501 non-null   int64 \n",
      " 1   year          1501 non-null   int64 \n",
      " 2   country       1501 non-null   object\n",
      " 3   country_name  1501 non-null   object\n",
      " 4   speaker       1495 non-null   object\n",
      " 5   position      892 non-null    object\n",
      " 6   text          1501 non-null   object\n",
      "dtypes: int64(2), object(5)\n",
      "memory usage: 93.8+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0fb8f8c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>session</th>\n",
       "      <th>year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1501.000000</td>\n",
       "      <td>1501.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>49.485010</td>\n",
       "      <td>1994.485010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>12.922149</td>\n",
       "      <td>12.922149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>25.000000</td>\n",
       "      <td>1970.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>39.000000</td>\n",
       "      <td>1984.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>51.000000</td>\n",
       "      <td>1996.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>61.000000</td>\n",
       "      <td>2006.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>70.000000</td>\n",
       "      <td>2015.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           session         year\n",
       "count  1501.000000  1501.000000\n",
       "mean     49.485010  1994.485010\n",
       "std      12.922149    12.922149\n",
       "min      25.000000  1970.000000\n",
       "25%      39.000000  1984.000000\n",
       "50%      51.000000  1996.000000\n",
       "75%      61.000000  2006.000000\n",
       "max      70.000000  2015.000000"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "65ddfd14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>session</th>\n",
       "      <th>year</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1501.000000</td>\n",
       "      <td>1501.000000</td>\n",
       "      <td>1501.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>49.485010</td>\n",
       "      <td>1994.485010</td>\n",
       "      <td>18047.099933</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>12.922149</td>\n",
       "      <td>12.922149</td>\n",
       "      <td>7996.150564</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>25.000000</td>\n",
       "      <td>1970.000000</td>\n",
       "      <td>2991.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>39.000000</td>\n",
       "      <td>1984.000000</td>\n",
       "      <td>11962.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>51.000000</td>\n",
       "      <td>1996.000000</td>\n",
       "      <td>16457.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>61.000000</td>\n",
       "      <td>2006.000000</td>\n",
       "      <td>22683.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>70.000000</td>\n",
       "      <td>2015.000000</td>\n",
       "      <td>60437.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           session         year        length\n",
       "count  1501.000000  1501.000000   1501.000000\n",
       "mean     49.485010  1994.485010  18047.099933\n",
       "std      12.922149    12.922149   7996.150564\n",
       "min      25.000000  1970.000000   2991.000000\n",
       "25%      39.000000  1984.000000  11962.000000\n",
       "50%      51.000000  1996.000000  16457.000000\n",
       "75%      61.000000  2006.000000  22683.000000\n",
       "max      70.000000  2015.000000  60437.000000"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['length'] = df['text'].str.len()\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "622bc380",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>country_name</th>\n",
       "      <th>speaker</th>\n",
       "      <th>position</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1501</td>\n",
       "      <td>1501</td>\n",
       "      <td>1495</td>\n",
       "      <td>892</td>\n",
       "      <td>1501</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>196</td>\n",
       "      <td>196</td>\n",
       "      <td>1359</td>\n",
       "      <td>43</td>\n",
       "      <td>1501</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>KHM</td>\n",
       "      <td>Cambodia</td>\n",
       "      <td>Tuilaepa Sailele Malielegaoi</td>\n",
       "      <td>Minister for Foreign Affairs</td>\n",
       "      <td>﻿The task of the President of the General Asse...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>16</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>339</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       country country_name                       speaker  \\\n",
       "count     1501         1501                          1495   \n",
       "unique     196          196                          1359   \n",
       "top        KHM     Cambodia  Tuilaepa Sailele Malielegaoi   \n",
       "freq        16           16                             5   \n",
       "\n",
       "                            position  \\\n",
       "count                            892   \n",
       "unique                            43   \n",
       "top     Minister for Foreign Affairs   \n",
       "freq                             339   \n",
       "\n",
       "                                                     text  \n",
       "count                                                1501  \n",
       "unique                                               1501  \n",
       "top     ﻿The task of the President of the General Asse...  \n",
       "freq                                                    1  "
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe(include='O')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2372dd75",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "session           0\n",
       "year              0\n",
       "country           0\n",
       "country_name      0\n",
       "speaker           6\n",
       "position        609\n",
       "text              0\n",
       "length            0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "d7ee8a33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "session         0\n",
       "year            0\n",
       "country         0\n",
       "country_name    0\n",
       "speaker         0\n",
       "position        0\n",
       "text            0\n",
       "length          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['speaker'].fillna('unknown', inplace=True)\n",
    "df['position'].fillna('unknown', inplace=True)\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5f95e763",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>session</th>\n",
       "      <th>year</th>\n",
       "      <th>country</th>\n",
       "      <th>country_name</th>\n",
       "      <th>speaker</th>\n",
       "      <th>position</th>\n",
       "      <th>text</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [session, year, country, country_name, speaker, position, text, length]\n",
       "Index: []"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['speaker'].str.contains('BUSH')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a01bd298",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['length'].plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "10d7b270",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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D4IefPDBIX9rt9ttHnzwwXH7jGi/v+muAoA09+KLL+rWW29VQ0ODJGnFihV68skntWLFCklSd3e3jDGSpMsuu0y33HLLkGusX79eS5Ys0ac//Wm9+OKLET/j05/+tJYsWaL169dLkq666ipdddVVcjgckqTi4mJJ0m9+8xutX79eDQ0Nam1t1YIFC/TWW2/prbfe0lVXXaWGhgbdeuutevHFF8Ouu23bNrW3t2vbtm1WW2699dYhr5WUlOixxx6Ty+WSw+HQjTfeqGeffVY33nijJKmkpCSq3yPS50V6D4K+/e1v67HHHlNxcbGeffZZ1dXV6dlnn1VxcbEee+wxffvb345vg8aSnEKrKr29vebBBx80lZWVJjc311x++eVm8+bN1rnPPfecKSoqMq+//rpZsGCBycvLM2vXrjW1tbXWOf39/ebee+81RUVFZsqUKebb3/62ueOOO8xf/uVfGmOMufPOO4ck8GPHjlmVnE2bNplly5aZnJwcs3LlSnPgwIGx/DpUcgCkPY/HY2bOnGlycnJMTk6OWbdunfF6vcYYY7q7u8P++5qdnW26u7tNVVWVuemmm0xZWZlxOBwmJyfHVFVVmb6+PnPzzTebWbNmGY/HE/YZVVVV5uabbzZ9fX3WY6/Xa/r6+kxOTo7Jzc01PT095uabbzZVVVVWm8rKysKu5/V6zbp160xubq6ZOXNm2LVChV63r69vyO9bVlZm3G532O/r9Xqtz1+3bt2Iv8fgzwu8d/B7ENTb22vcbrcpLy83/f39Ya/19/eb8vJy43a7TW9v73l/VrTf32MakxPqK1/5io4fP64XXnhBlZWVeumll3TDDTdoz549uvDCCyVJXV1d+uEPf6hf//rXcjqd+tKXvqRvfetbev755yVJ//zP/6znn39ezz33nC666CI9/vjjevnll7VmzRpJ0uOPP66DBw9q8eLF+sd//EdJUmlpqY4fPy5J+t73vqcf/ehHKi0t1V133aWvfvWr+tOf/jRsm3t7e9Xb22sdt7a2SpLa2tpivQ1x193n1bFzHYluRlJo6/bov481qaQgUxkuipJj1e/1yel0aMm0okQ3BeNsVkm+cjL940e2bt2qEydOWK898MAD6ujw/zfk6aefDntfT0+PfvKTn+j48eP6+c9/rurqaj3wwAPq7u7W8ePHtXHjRt133336i7/4C73++uvWmJqtW7da79m4caP1uKOjQ1u3blV3d7ckadOmTdb7Ax599FHdf//9Yde7//779eqrr1rtDlwrVOh1N27cGNaWEydO6J577tFPf/pTrV69Ouy9gc+/++679eqrrw77ewz+vND3hr4HQU8//bQ8Ho++973vqaura8jrDz30kB544AH9+Mc/1te//vXz+qzA97YZqEAOayzJKVDJOXz4sHE4HKampibs9euuu8489NBDxhh/JUeSOXz4sPX6U089ZcrLy63j8vJy89hjj1nHHo/HXHDBBVYlJ/QzQ4VWcgJ+97vfGUmmu7t72PY//PDDo/Y588MPP/zwww8/qfFz6tSpEXNLTJWcXbt2yRijefPmhT3f29tr9blKUm5urubMmWMdT506VfX19ZL8VZSzZ8/q8ssvt153uVxatmyZfD5fVO1YunRp2LUl/yj+Cy64IOL5Dz30kL7xjW9Yxz6fT01NTSouLrb6jMdLW1ubZsyYoVOnTqmwsHBcr51OuE/R415Fh/sUPe5V9LhX0YnXfTLGqL29XZWVlSOeF1PI8fl8crlc2rlz55Apdfn5+dbjjIyMsNccDseQ0tLgcDH49ZGEXj9wnZECUlZWlrKyssKes3sKemFhIf+HiAL3KXrcq+hwn6LHvYoe9yo68bhPRUVFo54T00CGSy+9VF6vV/X19Zo7d27YT0VFRdSNKy8v144dO6znvF6v3n///bDzMjMz5fV6Y2kmAACYwGKq5MybN0+33Xab7rjjDv3oRz/SpZdeqnPnzuntt9/WkiVL9MlPfjKq69x7771av3695s6dqwULFujJJ59Uc3NzWHWnqqpK27dv1/Hjx5Wfn68pU6bE0mQAADDBxDwl5bnnntMdd9yhb37zm5o/f75uueUWbd++XTNmzIj6Gt/5znf0hS98QXfccYdWrlyp/Px8rV27VtnZ2dY53/rWt+RyubRw4UKVlpbq5MmTsTY5rrKysvTwww8P6R5DOO5T9LhX0eE+RY97FT3uVXSS7T45zFgGwdjM5/Ppoosu0mc/+1l9//vfT3RzAABACot5nZzxcOLECW3cuFHXXHONent79dOf/lTHjh3TF7/4xUQ2CwAApIGErqDmdDr17//+77rssst05ZVXas+ePdq0aZMuuuiiRDYLAACkgaTqrgIAABgvrIUPAADSEiHHBk8//bRmzZql7OxsLVu2TFu3bk10k8bNH/7wB918882qrKyUw+HQyy+/HPa6MUaPPPKIKisrlZOTo9WrV2vv3r1h5/T29uree+9VSUmJ8vLydMstt+j06dNh5zQ3N+v2229XUVGRioqKdPvtt6ulpSXsnJMnT+rmm29WXl6eSkpKdN9996mvr8+OXzsm69ev12WXXaaCggKVlZXpr/7qr/TRRx+FncP9kp555hktXbrUWjxs5cqV+v3vf2+9zj2KbP369XI4HHrggQes57hXfo888ogcDkfYT+gabtyncDU1NfrSl76k4uJi5ebm6pJLLtHOnTut11P6fo246QPG7IUXXjAZGRnm2WefNfv27TP333+/ycvLMydOnEh008bFa6+9Zr73ve+ZDRs2GEnmpZdeCnv90UcfNQUFBWbDhg1mz5495nOf+5yZOnWqaWtrs8656667zLRp08ybb75pdu3aZdasWWMuvvjisJ19b7jhBrN48WLz7rvvmnfffdcsXrzYrFu3znrd4/GYxYsXmzVr1phdu3aZN99801RWVpp77rnH9nsQrbVr15rnnnvOVFdXmw8++MDcdNNN5oILLjAdHR3WOdwvY1555RXzu9/9znz00Ufmo48+Mt/97ndNRkaGqa6uNsZwjyLZsWOHqaqqMkuXLg3b24975ffwww+bRYsWmbq6Ouunvr7eep37FNTU1GRmzpxpvvzlL5vt27ebY8eOmU2bNoXtO5nK94uQM84uv/xyc9ddd4U9t2DBAvP3f//3CWqRfQaHHJ/PZyoqKsyjjz5qPdfT02OKiorMv/zLvxhjjGlpaTEZGRnmhRdesM6pqakxTqfTvP7668YYY/bt22ckmffee886Z9u2bUaSOXDggDHGH7acTmfYJrH/8R//YbKyskxra6stv+/5qq+vN5LMO++8Y4zhfo1k8uTJ5uc//zn3KIL29nZz4YUXmjfffDNsA2PuVdDDDz9sLr744oivcZ/Cfec73zFXXXXVsK+n+v2iu2oc9fX1aefOnbr++uvDnr/++uv17rvvJqhV8XPs2DGdOXMm7PfPysrSNddcY/3+O3fuVH9/f9g5lZWVWrx4sXXOtm3bVFRUpCuuuMI6Z8WKFSoqKgo7Z/HixWGbs61du1a9vb1hZdZk0traKknWqt3cr6G8Xq9eeOEFdXZ2auXKldyjCO6++27ddNNN+sQnPhH2PPcq3KFDh1RZWalZs2bp85//vI4ePSqJ+zTYK6+8ouXLl+szn/mMysrKdOmll+rZZ5+1Xk/1+0XIGUfnzp2T1+tVeXl52PPl5eU6c+ZMgloVP4HfcaTf/8yZM8rMzNTkyZNHPKesrGzI9cvKysLOGfw5kydPVmZmZlLea2OMvvGNb+iqq67S4sWLJXG/Qu3Zs0f5+fnKysrSXXfdpZdeekkLFy7kHg3ywgsvaNeuXVq/fv2Q17hXQVdccYV+9atf6Y033tCzzz6rM2fOaNWqVWpsbOQ+DXL06FE988wzuvDCC/XGG2/orrvu0n333adf/epXklL/31VCFwNMV5F2Vh/8XDqL5fcffE6k82M5J1ncc8892r17t/74xz8OeY37Jc2fP18ffPCBWlpatGHDBt1555165513rNe5R9KpU6d0//33a+PGjWFb3wzGvZJuvPFG6/GSJUu0cuVKzZkzR7/85S+1YsUKSdynAJ/Pp+XLl+sHP/iBJP8G3Hv37tUzzzyjO+64wzovVe8XlZxxVFJSIpfLNSRx1tfXD0mn6Sgwe2Gk37+iokJ9fX1qbm4e8ZyzZ88OuX5DQ0PYOYM/p7m5Wf39/Ul3r++991698sor2rx5s6ZPn249z/0KyszM1Ny5c7V8+XKtX79eF198sR5//HHuUYidO3eqvr5ey5Ytk9vtltvt1jvvvKMnnnhCbrfbaiP3aqi8vDwtWbJEhw4d4t/UIFOnTtXChQvDnrvooousfSJT/X4RcsZRZmamli1bpjfffDPs+TfffFOrVq1KUKviZ9asWaqoqAj7/fv6+vTOO+9Yv/+yZcuUkZERdk5dXZ2qq6utc1auXKnW1lbt2LHDOmf79u1qbW0NO6e6ulp1dXXWORs3blRWVpaWLVtm6+8ZLWOM7rnnHr344ot6++23NWvWrLDXuV/DM8aot7eXexTiuuuu0549e/TBBx9YP8uXL9dtt92mDz74QLNnz+ZeDaO3t1f79+/X1KlT+Tc1yJVXXjlkaYuDBw9q5syZktLgv1MxDVfGsAJTyH/xi1+Yffv2mQceeMDk5eWZ48ePJ7pp46K9vd28//775v333zeSzI9//GPz/vvvW1PkH330UVNUVGRefPFFs2fPHvOFL3wh4lTD6dOnm02bNpldu3aZa6+9NuJUw6VLl5pt27aZbdu2mSVLlkScanjdddeZXbt2mU2bNpnp06cn1dTMr33ta6aoqMhs2bIlbCprV1eXdQ73y5iHHnrI/OEPfzDHjh0zu3fvNt/97neN0+k0GzduNMZwj0YSOrvKGO5VwDe/+U2zZcsWc/ToUfPee++ZdevWmYKCAuu/w9ynoB07dhi3223+6Z/+yRw6dMg8//zzJjc31/zmN7+xzknl+0XIscFTTz1lZs6caTIzM83HPvYxa8pwOti8ebORNOTnzjvvNMb4pxs+/PDDpqKiwmRlZZmrr77a7NmzJ+wa3d3d5p577jFTpkwxOTk5Zt26debkyZNh5zQ2NprbbrvNFBQUmIKCAnPbbbeZ5ubmsHNOnDhhbrrpJpOTk2OmTJli7rnnHtPT02Pnrz8mke6TJPPcc89Z53C/jPnqV79q/f+ltLTUXHfddVbAMYZ7NJLBIYd75RdYxyUjI8NUVlaaT33qU2bv3r3W69yncP/1X/9lFi9ebLKyssyCBQvMz372s7DXU/l+sXcVAABIS4zJAQAAaYmQAwAA0hIhBwAApCVCDgAASEuEHAAAkJYIOQAAIC0RcgAAQFoi5AAAgLREyAEAAGmJkAMAANISIQcAAKQlQg4AAEhL/z/IaPLH02uX8gAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['length'].plot()\n",
    "df['length'].plot(kind='box', vert=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a21a6037",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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P3r06HTLLbekIUOGdNg2ePDgDsfqbP8t++js9kWLFnV6n8N9PAc75qHuR+duueWWDl8TJSUl6ZZbbvnAjnG4P7/9ugrgBLd48eK48sorY/v27XH22WdHRMTEiRPj3HPP7TD2zDPPjJtvvjn69u0bERHNzc0REfHQQw/FypUrY9y4cfGFL3whFi9e3OlxvvCFL8S4ceNi5cqV8dBDD0VExMCBA6OoqCgiIiZPnhyTJ0+OiIg5c+bEoEGD4p577om6urqYPHly/PKXv4xf/vKXMXny5Ni+fXtceeWVhWO13//u3btj5cqVhX0MGjSoze0tc73yyitj0KBBUVRUFJdffnnMnz8/Lr/88oiIGDRoUJeP52DHPNg60LVbb7017rnnnhg4cGDMnz8/tmzZEvPnz4+BAwfGPffcE7feeuuxndCRlFPrsyqNjY3plltuSZWVlalPnz7poosuSsuXLy+MXbBgQaqoqEhPPPFE+shHPpL69u2bLrvssrR58+bCmP3796cbbrghVVRUpAEDBqRbb701XXPNNelzn/tcSimla6+9tkOVb9iwoXAmZ9myZWn8+PGpvLw8TZw4Mb300ktH8nCcyekBx9O6OJPDiaSr/+sDBw6kUaNGpfLy8jR9+vQ0atSodMUVV6SmpqbU0NDQ4czJmDFjUmNjYzrjjDNSaWlpKioqSuXl5Wn06NHpwIEDqampKV1xxRVpzJgx6cCBA22OM3r06MK+W3++d+/eVF5envr06ZP27dtX2Mfo0aPTqFGjUnFxcSovL0/79u0r7K+pqSlVV1enPn36pNGjR6fGxsY2+2//+IYOHdphTvv27Uvl5eWF+be+b+s5VFdXd7hvZ4+pta7Wga41NjamkpKSNHTo0LR///422/bv35+GDh2aSkpKUmNj4/s+1uH+/D6i1+S09td//dexcePGWLhwYVRWVsajjz4an/nMZ2Lt2rVx1llnRUTEnj174t57743/+I//iOLi4vjSl74Us2bNiocffjgiIu6+++54+OGHY8GCBXH22WfH/fffH4899lhMmzYtIiLuv//++P3vfx9VVVXxne98JyIiBg8eHBs3boyIiG9961tx3333xeDBg+P666+Pr3zlK/Hcc891OefGxsZobGwsfL5r167uPvxD2rv/vT+i92qdvzPTWst6tKwP74+vs5NHV987zz77bLz++usREfHZz342li5dGgsXLozi4uJ48MEH24y95ppr4r777ou5c+fGG2+8Ebfddlvcfffd0dDQEBs3boxnn302pk6dGrfffntMmjSp8HnLcTZu3BiPPPJIFBcXx4oVKwqfr1y5MhoaGiIi4rnnnmuzjxYNDQ2FbRERxcXFcccdd0RNTU1s3Lgx5s6d22b/7R/fvHnz4rrrrmszp+eee65w3Pb3LS4uLsxh1qxZUVNT0+a+nT2m1lrfv/396NzcuXPjwIEDMXv27CgpaZsXJSUl8Z3vfCf+/u//PubOnRs33XTTMZlTtyLntddei0ceeSTeeuutqKysjIiIWbNmxRNPPBELFiyI733vexERsX///njwwQdj7NixERExc+bMQqxERPzoRz+K22+/Pf70T/80IiJ+/OMfx89//vPC9oqKiigtLY0+ffrEsGHDOszju9/9bkyZMiUiIr75zW/G9OnTY+/evXHKKad0Ou85c+bEP/3TP3XnIR+xt3a8941308/WHJPjnWje2tEQE0b39CxOfL7OTj7tv3e2bNlS+Hd5eXlERFRVVUXEe8/VrX3oQx9qc/vf/M3fxN13391hXy33b73vrrZVVVXFkiVLuhzXWuv9tR/TMqf292u5T3V1dZdz6mx/rT9vWZf24w8219a3t78fnWv5P2z5v2qv5fb2X5dHU7ciZ9WqVZFSij/+4z9uc3tjY2MMHDiw8HmfPn0KgRMRMXz48Kirq4uIiPr6+ti2bVtcdNFFhe29evWK8ePHF35HfCitf988fPjwiHjvFf1nnHFGp+Nvv/32uPnmmwuf79q1K0aOHHlYxzpSI05775vqh1edH2cOOfWoHONE9GrdO3HTz9YU1of3x9fZyaOr752W576IKJzVWLduXVxyySVtnn8jItavXx8RUbj93/7t3zrd17p16zrsu/W2Sy65pM3nXY1rr/W49mNa5tSy//b3qamp6XJOrffX+r4t+29Zl/bj2z+m9jpbB7rW8n9YU1MTf/u3f9the8v/Yfuvy6PqSH4H1vKanIULF6ZevXqll156Kb3yyittPrZs2ZJS+v/X5LT26KOPppZD7ty5M0VEeuaZZ9qMmTFjRuE1Oa2P2Vpn765avXp14TU7h8trco6942ldvCaHE4nX5HhNzvHueHxNTrfeXXXBBRdEU1NT1NXVxZlnntnmo7NfK3WmoqIihg4d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AwBkSeQAAFkSOQBAlkQOAJClkp6eQE9KKUVExK5du3p4JgDA4Wr5ud3yc7wrJ3Xk7N69OyIiRo4c2cMzAQCO1O7du6OioqLL7UXpUBmUsebm5ti8eXP069cvioqKeno6J4xdu3bFyJEj480334z+/fv39HROGNat+6xd91i37rN23XOs1i2lFLt3747KysooLu76lTcn9Zmc4uLiGDFiRE9P44TVv39/3/zdYN26z9p1j3XrPmvXPcdi3Q52BqeFFx4DAFkSOQBAlkQOR6ysrCzuvPPOKCsr6+mpnFCsW/dZu+6xbt1n7brneFu3k/qFxwBAvpzJAQCyJHIAgCyJHAAgSyIHAMiSyDkJPPPMM3HFFVdEZWVlFBUVxWOPPdZme0opvv3tb0dlZWWUl5fH1KlT48UXX2wzprGxMW644YYYNGhQ9O3bN/7kT/4k3nrrrTZjduzYEV/+8pejoqIiKioq4stf/nLs3LmzzZg33ngjrrjiiujbt28MGjQovva1r8W+ffuOxsN+3+bMmRMXXnhh9OvXL4YMGRIzZsyIl19+uc0Ya9fRAw88EOeee27hYmATJ06M//zP/yxst2aHb86cOVFUVBQ33XRT4Tbr19G3v/3tKCoqavMxbNiwwnZrdnCbNm2KL33pSzFw4MDo06dPnH/++fHCCy8Utp/Q65fI3s9//vP0rW99Ky1atChFRHr00UfbbL/rrrtSv3790qJFi9LatWvTVVddlYYPH5527dpVGHP99den008/PT311FNp1apVadq0aem8885LBw4cKIz5zGc+k6qqqtLzzz+fnn/++VRVVZWqq6sL2w8cOJCqqqrStGnT0qpVq9JTTz2VKisr08yZM4/6GnTHZZddlhYsWJDWrVuX1qxZk6ZPn57OOOOM9M477xTGWLuOHn/88bR06dL08ssvp5dffjndcccdqXfv3mndunUpJWt2uGpra9Po0aPTueeem2688cbC7davozvvvDN99KMfTVu2bCl81NXVFbZbs679z//8Txo1alT6q7/6q/Sb3/wmbdiwIS1btiy9+uqrhTEn8vqJnJNM+8hpbm5Ow4YNS3fddVfhtr1796aKior04IMPppRS2rlzZ+rdu3dauHBhYcymTZtScXFxeuKJJ1JKKf3ud79LEZF+/etfF8asXLkyRUR66aWXUkrvxVZxcXHatGlTYcwjjzySysrKUn19/VF5vB+kurq6FBHp6aefTilZuyNx2mmnpX/913+1Zodp9+7d6ayzzkpPPfVUmjJlSiFyrF/n7rzzznTeeed1us2aHdxtt92WJk+e3OX2E339/LrqJLdhw4bYunVrfPrTny7cVlZWFlOmTInnn38+IiJeeOGF2L9/f5sxlZWVUVVVVRizcuXKqKioiIsvvrgw5pJLLomKioo2Y6qqqqKysrIw5rLLLovGxsY2p0aPV/X19RERMWDAgIiwdoejqakpFi5cGO+++25MnDjRmh2mr371qzF9+vT41Kc+1eZ269e1V155JSorK2PMmDHxxS9+MdavXx8R1uxQHn/88ZgwYUL82Z/9WQwZMiQuuOCCmD9/fmH7ib5+Iuckt3Xr1oiIGDp0aJvbhw4dWti2devWKC0tjdNOO+2gY4YMGdJh/0OGDGkzpv1xTjvttCgtLS2MOV6llOLmm2+OyZMnR1VVVURYu4NZu3ZtnHrqqVFWVhbXX399PProo3HOOedYs8OwcOHCWLVqVcyZM6fDNuvXuYsvvjh++tOfxi9+8YuYP39+bN26NSZNmhRvv/22NTuE9evXxwMPPBBnnXVW/OIXv4jrr78+vva1r8VPf/rTiDjxv+ZO6r9Czv8rKipq83lKqcNt7bUf09n47ow5Hs2cOTN++9vfxq9+9asO26xdRx/+8IdjzZo1sXPnzli0aFFce+218fTTTxe2W7POvfnmm3HjjTfGk08+GaecckqX46xfW5dffnnh3+PGjYuJEyfG2LFj49///d/jkksuiQhr1pXm5uaYMGFCfO9734uIiAsuuCBefPHFeOCBB+Kaa64pjDtR18+ZnJNcyzsQ2ldyXV1doaiHDRsW+/btix07dhx0zLZt2zrsf/v27W3GtD/Ojh07Yv/+/R3q/Xhyww03xOOPPx7Lly+PESNGFG63dl0rLS2NM888MyZMmBBz5syJ8847L+6//35rdggvvPBC1NXVxfjx46OkpCRKSkri6aefjn/5l3+JkpKSwryt38H17ds3xo0bF6+88oqvuUMYPnx4nHPOOW1uO/vss+ONN96IiBP/eU7knOTGjBkTw4YNi6eeeqpw2759++Lpp5+OSZMmRUTE+PHjo3fv3m3GbNmyJdatW1cYM3HixKivr4/a2trCmN/85jdRX1/fZsy6detiy5YthTFPPvlklJWVxfjx44/q4+yOlFLMnDkzFi9eHP/1X/8VY8aMabPd2h2+lFI0NjZas0O49NJLY+3atbFmzZrCx4QJE+Lqq6+ONWvWxIc+9CHrdxgaGxvjv//7v2P48OG+5g7hYx/7WIdLY/z+97+PUaNGRUQGz3PderkyJ5Tdu3en1atXp9WrV6eISD/4wQ/S6tWr0+uvv55Seu/tgRUVFWnx4sVp7dq16S/+4i86fXvgiBEj0rJly9KqVavSJz/5yU7fHnjuueemlStXppUrV6Zx48Z1+vbASy+9NK1atSotW7YsjRgx4rh9e+U//MM/pIqKirRixYo2b03ds2dPYYy16+j2229PzzzzTNqwYUP67W9/m+64445UXFycnnzyyZSSNTtSrd9dlZL168w3vvGNtGLFirR+/fr061//OlVXV6d+/fqljRs3ppSs2cHU1tamkpKS9N3vfje98sor6eGHH059+vRJDz30UGHMibx+IucksHz58hQRHT6uvfbalNJ7bxG8884707Bhw1JZWVn6xCc+kdauXdtmHw0NDWnmzJlpwIABqby8PFVXV6c33nijzZi33347XX311alfv36pX79+6eqrr047duxoM+b1119P06dPT+Xl5WnAgAFp5syZae/evUfz4XdbZ2sWEWnBggWFMdauo6985Stp1KhRqbS0NA0ePDhdeumlhcBJyZodqfaRY/06arluS+/evVNlZWX6/Oc/n1588cXCdmt2cEuWLElVVVWprKwsfeQjH0nz5s1rs/1EXr+ilFLq3jkgAIDjl9fkAABZEjkAQJZEDgCQJZEDAGRJ5AAAWRI5AECWRA4AkCWRAwBkSeQAAFkSOQBAlkQOAJAlkQMAZOl/AddGlgfxSJqbAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['length'].plot(kind='box', vert=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "c09a2632",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['length'].plot(kind='hist', bins=30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "e0b1d209",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\jyoth\\anaconda3\\Lib\\site-packages\\seaborn\\axisgrid.py:118: UserWarning: The figure layout has changed to tight\n",
      "  self._figure.tight_layout(*args, **kwargs)\n"
     ]
    },
    {
     "data": {
      "image/png": "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PPFEs/fNmzdP3/72twN+drlcuuOOOwLqysrK5HK59Omnn7bhWcA05/N7zeVy6eWXX2723ry8PA0dOtT+uaqqSrfffrt69Oght9ut+Ph4ZWZmauvWre1wJjBNZWWlfvazn+mqq66Sx+NRXFycvv/97+v//J//o3/+85+Svv69d+L6DAoKUmJioqZOnRpwfW7atCng73W3bt00fPhw/eUvf3Hq1IxFsINj5s2bpyeeeEK//vWvtWfPHr355pvKzc097f/JXrNmjVJTU5WSkqI//vGPDnQLk4wePVoVFRUBS69evQK2ffrpp/qv//ovvfrqq5o+fXqzfXDN4UJ8+umnSktL0xtvvKFFixZp165dKiws1LBhwzRjxowL3p/H49Hy5cv10UcftUG3uNSc7++1c7nlllv017/+Vc8//7w++ugjvfLKKxo6dKgOHz7cBl3DZH//+9/1ne98R8XFxVqwYIHee+89bdy4UT//+c/16quvauPGjXbtf/7nf6qiokIHDhzQ6tWr9dZbb2nWrFnN9rlv3z5VVFRo06ZNuuKKKzR27FhVVVW152kZL9jpBtB5nfjD84Mf/MBed+211562dvny5frRj34ky7K0fPly3Xrrre3VJgx04r80n2tb9+7dNWnSJK1YsaJZHdccLsT06dPlcrm0Y8cOhYeH2+uvueYa3XbbbRe8v+TkZMXGxupXv/qV/u///b+t2SouQef7e+1sjhw5opKSEm3atEk33HCDJKlnz5763ve+19rt4hIwffp0BQcH65133gn4ndevXz/dcsstOvmm+xEREfb1+Y1vfEM//vGPVVBQ0GyfsbGxuvzyyxUfH2//7tu+fbvGjRvX9id0iWDEDo6Jj4/XG2+8oUOHDp217pNPPtHWrVs1ceJETZw4UVu2bNHf//73duoSl7K///3vKiwsVNeuXQPWc83hQhw+fFiFhYWaMWNGwP/BOeHyyy9v0X5/85vfaM2aNdq5c+dFdojO5Ey/187lsssu02WXXaaXX35Zfr+/jbrDpeDLL79UcXHxGX/nSbK/dnOqf/zjH3rttdc0cODAM+7/n//8p/21nAu9jjs7gh0c8/jjj+vQoUOKj49X//79dccdd+hPf/pTs7r//u//1pgxY+zvO40ePVr//d//7UDHMMVrr71m/5+Uyy67LGBU+MS20NBQXXnlldqzZ4/uvvvugPdzzeFC/O1vf5NlWbr66qvPWXv33XcHXJuXXXaZFixYcNra7373u5o4caJ++ctftnbLuMScz++1cwkODtaKFSv0/PPP6/LLL9eQIUN0zz336P3332+jrmGqE7/zkpOTA9bHxMTYv9dOvv5O/N4LDQ1V9+7d5XK59Pjjjzfbb/fu3e33L168WGlpaRoxYkSbn8+lhGAHx6SkpGj37t3atm2bfvKTn+jgwYMaN26c/uM//sOuaWpq0vPPP68f/ehH9rof/ehHev7559XU1ORE2zDAsGHDVFZWZi9PPvlks23bt2/XzJkzlZmZqZkzZ9rbueZwoU5MOTrTf6E+2S9+8YuAa7OsrKzZTVJO9tBDD+ntt99WcXFxq/WLS8+5fq+dr1tuuUVffPGFXnnlFWVmZmrTpk367ne/e8HTOtE5nPo7b8eOHSorK9M111wTMOp74vfe+++/b99MauzYsc3+pr799tt699139fvf/149e/bUihUrGLG7QAQ7tInIyEj5fL5m648cOaLIyEj75y5duui6667Tz3/+c61du1YrVqzQ8uXLtX//fklSUVGR/vGPf2jSpEkKDg5WcHCwfvjDH+rzzz/n/+jgjMLDw3XVVVfZS0JCQrNt/fv315NPPim/368HH3zQ3s41hwvVu3dvuVwu7d2795y1MTExAdfmVVddpejo6DPWX3nllcrNzdUvf/nLgO+sACc71++1iIiIM/5N9nq9Aes8Ho9GjRql+++/X1u2bNGUKVP0wAMPtPk5wBxXXXWVXC6XPvzww4D13/rWt3TVVVcpNDQ0YP2J33u9e/fW8OHD9cQTT2jLli168803A+p69eqlPn36aNKkSXrwwQd10003MS34AhHs0CauvvpqvfPOO83W79y5s9nQ/clSUlIkSceOHZP09Q0sfvjDHzb7L9y33nqrli9f3jbNo1N54IEH9Oijj+qLL76QxDWHCxcdHa3MzEz97ne/s393nezIkSMXtf/7779fH3300WlvNgCczqm/166++upm39W0LEulpaVn/Zssff13+XTXNTqvbt26adSoUVqyZEmLro2goCBJOuujhHJycnT8+HE9/fTTLe6zMyLYoU1Mnz5dn3zyiWbMmKG//vWv+uijj/S73/1Oy5cv1y9+8QtJ0r//+79r8eLF2r59uz777DNt2rRJM2bMUJ8+fXT11Vfr0KFDevXVVzV58mSlpqYGLJMnT9Yrr7xyzhuvAOcydOhQXXPNNVqwYAHXHFrs6aefVlNTk773ve9pzZo1+vjjj7V37149+eSTSk9Pv6h9x8XFafbs2QFTioGzOfn3miTl5+dr+fLlWrJkiT766CP99a9/1Z133mn/nZa+viHG8OHDtWrVKr3//vvav3+//vCHP2jRokWaMGGCk6eDDujpp5/WV199pQEDBuill17S3r17tW/fPq1atUoffvihHd4k6ejRo6qsrFRFRYV27NihX/ziF4qJidHgwYPPuP8uXbooLy9Pv/nNb+xn4uHcCHZoE9/85jf19ttv65NPPlFGRoauu+46rVixQitWrLBvZJGZmalXX31V48aNU58+fTR58mRdffXVKi4uVnBwsF544QWFh4ef9ouzw4YNU0REhFauXNnep4ZL0OzZs7Vs2TI9/fTTXHNokV69eundd9/VsGHDNGfOHKWmpmrUqFH685//rGeeeeai9/+LX/xCl112WSt0is7ixO+18vJyTZw40b4xynXXXaeMjAx98sknevvtt9WzZ09JX98Vc+DAgVq8eLGuv/56paam6r777lNubq6WLFni8Nmgo7nyyiv13nvvaeTIkZo7d66uvfZaDRgwQE899ZTy8/P161//2q69//77lZCQoMTERGVlZSk8PFwbNmxQt27dznqM2267TY2NjVx/F8BlMWkfAAAAAIzGiB0AAAAAGI5gBwAAAACGI9gBAAAAgOEIdgAAAABgOIIdAAAAABiOYAcAAAAAhiPYAQAAAIDhCHYAAAAAYDiCHQAAAAAYjmAHAEAH8+mnn8rlcqmsrMzpVgAAhiDYAQBgqIaGBqdbAAB0EAQ7AABOcfz4cT388MO66qqr5Ha71aNHD82fP1+StGvXLg0fPlyhoaHq1q2bpk2bptraWvu9Q4cOVV5eXsD+brzxRk2ZMsX++Zvf/KYWLFig2267TREREerRo4eeffZZe3uvXr0kSd/5znfkcrk0dOhQSdKUKVN04403auHChUpMTFSfPn30n//5n+rXr1+zc0hLS9P999/fSp8IAKCjI9gBAHCKuXPn6uGHH9Z9992nPXv26MUXX1RcXJz++c9/avTo0YqKitLOnTv1hz/8QRs3btSdd955wcd47LHHNGDAAL333nuaPn26fvrTn+rDDz+UJO3YsUOStHHjRlVUVOiPf/yj/b4///nP2rt3rzZs2KDXXntNt912m/bs2aOdO3faNe+//77ee++9gDAJALi0BTvdAAAAHcnRo0f129/+VkuWLNHkyZMlSVdeeaW+//3va9myZaqrq9MLL7yg8PBwSdKSJUs0btw4Pfzww4qLizvv4/zbv/2bpk+fLkm6++67tXjxYm3atElXX321rrjiCklSt27dFB8fH/C+8PBw/dd//ZdCQkLsdZmZmXruued03XXXSZKee+453XDDDfrWt77V8g8CAGAURuwAADjJ3r175ff7NWLEiNNuu/baa+1QJ0lDhgzR8ePHtW/fvgs6Tv/+/e3XLpdL8fHxqqqqOuf7+vXrFxDqJCk3N1e///3vVV9fr8bGRq1evVq33XbbBfUDADAbI3YAAJwkNDT0jNssy5LL5TrtthPru3TpIsuyArY1NjY2q+/atWuz9x8/fvyc/Z0cKk8YN26c3G631q5dK7fbLb/fr1tuueWc+wIAXDoYsQMA4CS9e/dWaGio/vznPzfblpKSorKyMh07dsxe95e//EVdunRRnz59JElXXHGFKioq7O1NTU3avXv3BfVwYkSuqanpvOqDg4M1efJkPffcc3ruuef0wx/+UGFhYRd0TACA2RixAwDgJB6PR3fffbfuuusuhYSEaMiQITp06JA++OAD3XrrrXrggQc0efJkzZs3T4cOHdLMmTOVk5Njf79u+PDhmj17ttavX68rr7xSixcv1pEjRy6oh9jYWIWGhqqwsFDdu3eXx+OR1+s963v+4z/+Q3379pX0ddgEAHQujNgBAHCK++67T3PmzNH999+vvn37atKkSaqqqlJYWJiKiop0+PBhXXfddfr3f/93jRgxQkuWLLHfe9ttt2ny5Mn68Y9/rBtuuEG9evXSsGHDLuj4wcHBevLJJ7V06VIlJiZqwoQJ53xP7969NXjwYCUnJ2vgwIEXfM4AALO5rFO/CAAAAIxjWZauvvpq3X777Zo9e7bT7QAA2hlTMQEAMFxVVZVWrlypf/zjH/rJT37idDsAAAcQ7AAAMFxcXJxiYmL07LPPKioqyul2AAAOINgBAGA4vlUBAODmKQAAAABgOIIdAAAAABiOYAcAAAAAhiPYAQAAAIDhCHYAAAAAYDiCHQAAAAAYjmAHAAAAAIYj2AEAAACA4Qh2AAAAAGC4/w/CwmcdFu8+lgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x800 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "where = df['country'].isin(['USA', 'FRA', 'GBR', 'CHN', 'RUS'])\n",
    "g = sns.catplot(data=df[where], x=\"country\", y=\"length\", kind='box')\n",
    "g.fig.set_size_inches(10, 8) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b01e1adb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
