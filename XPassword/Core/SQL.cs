using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Data;
using System.Data.SqlClient;


namespace SpaceBaseApp.Core
{
    class SQL
    {
        //public static SqlConnection connect { get; set; }

        static SQL()
        {
            if (Environment.MachineName == "104-04")
            {
                connect = new SqlConnection(@"data source=104-04\SQLEXPRESS01;initial catalog=XPassword;integrated security=True;MultipleActiveResultSets=True;App=EntityFramework");
            }
            else if (Environment.MachineName == "212-01")
            {
                connect = new SqlConnection(@"data source=212-01\SQLEXPRESS;initial catalog=XPassword;integrated security=True;MultipleActiveResultSets=True;App=EntityFramework");
            }
            else 
            { 
            connect = new SqlConnection(@"data source=TIMUR-HOME\SqlExpress;initial catalog=XPassword;integrated security=True;MultipleActiveResultSets=True;App=EntityFramework");
            }
        }


        public static SqlConnection connect;


        public static void SQLConnect()
        {
            try
            {
                if (connect.State != ConnectionState.Open)
                {
                    connect.Open();
                }
            }
            catch (Exception)
            {
                Close();
                throw;
            }
        }


        public static DataTable Inquiry(string sql) //Возвращаем результат запроса
        {
            DataTable inv = new DataTable();

            try
            {
                using (SqlCommand cmd = new SqlCommand(sql, connect))
                {
                    SqlDataReader result = cmd.ExecuteReader();
                    inv.Load(result);
                    return inv;
                }
            }
            catch (Exception)
            {
                Close();
                return null;
            }

        }

        public static bool Execute(string sql)
        {
            try
            {

                using (SqlCommand cmd = new SqlCommand(sql, connect))
                {
                    cmd.ExecuteNonQuery();
                    return true;
                }
            }
            catch (Exception)
            {
                Close();
                return false;
            }
        }

        public static void Close()
        {
            try
            {
                connect.Close();
            }
            catch (Exception)
            {
                return;
            }
        }

    }
}
