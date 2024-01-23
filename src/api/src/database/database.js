const { Pool } = require("pg");
const dotenv = require("dotenv");
dotenv.config();
 
const connectDb = async () => {
    try {
        const pool = new Pool({
            user: "postgres",
            host: "localhost",
            database: "postgres",
            password: "postgres",
            port: process.env.PGPORT,
        });
 
        await pool.connect()
        const res = await pool.query('SELECT * FROM clients')
        console.log(res)
        await pool.end()
    } catch (error) {
        console.log(error)
    }
}
 
connectDb()