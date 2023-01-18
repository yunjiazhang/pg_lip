# pg_lip_bloom
The LIP extension for PostgreSQL

## Prepare PostgreSQL
Clone the code base of the PostgreSQL
```bash
wget https://ftp.postgresql.org/pub/source/v12.5/postgresql-12.5.tar.gz
tar xzvf postgresql-12.5.tar.gz
```
Compile and install 
```
cd postgresql-12.5
./configure --prefix=/data/postgresql-12.5 --without-readline
sudo make -j
sudo make install
echo 'export PATH=/data/postgresql-12.5/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Compile and install 
We use Makefile to make the installation procedure fluent. The default PostgreSQL installation directory ```/data/postgresql-12.5```. If you use other directories, change the ```PG_DIR``` in ```Makefile```.

Specifically, 1) run ```make``` to compile; 2) run ```make install``` to copy the compiled files to PostgreSQL directory; 3) run ```make clean``` to clean the compiled files.

## Usage example
To use ```pg_lip```, we need to first rewrite the query with the extension functions provided, then the query can be directly run with the PostgreSQL. 

![Alt text](docs/query_example.jpg?raw=true "Query rewriting example")

### Auto query rewriting
For JOB queries, we provide a auto query rewriting tool ```./lip_query_rewriter/rewriter.py```. The main function rewrites all the queries in ```all_files``` and output the rewriten queries to the subdir ```lip_auto_rewrite/```. Note that this rewriter needs to interact with PostgreSQL and only works on JOB queries. 
