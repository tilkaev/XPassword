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

        private SqlConnection connect = new SqlConnection(@"data source=25.68.7.66\SqlExpress;initial catalog=XPassword;user id=user;password=124279123;MultipleActiveResultSets=True;App=EntityFramework");

        /*
         SqlConnection connect = new SqlConnection(@"data source=10.10.10.21\SqlExpress;initial catalog=taxi;user id=user;password=124279123;MultipleActiveResultSets=True;App=EntityFramework");
            connect.Open();
            dt = new DataTable();

            SqlCommand cmd = new SqlCommand(sql, connect);
            dt.Load(cmd.ExecuteReader());
            main_data_grid.ItemsSource = dt.AsDataView();

            connect.Close();
         */

        public void SQLConnect()
        {
            try
            {
                connect.Open();
            }
            catch (Exception)
            {
                this.Close();
                throw;
            }
        }


        public DataTable Inquiry(string sql) //Возвращаем результат запроса
        {
            DataTable inv = new DataTable();

            try
            {
                using (SqlCommand cmd = new SqlCommand(sql, this.connect))
                {
                    SqlDataReader result = cmd.ExecuteReader();
                    inv.Load(result);
                    return inv;
                }
            }
            catch (Exception)
            {
                this.Close();
                throw;
            }

        }

        public bool Execute(string sql)
        {
            try
            {

                using (SqlCommand cmd = new SqlCommand(sql, this.connect))
                {
                    cmd.ExecuteNonQuery();
                    return true;
                }
            }
            catch (Exception)
            {
                this.Close();
                throw;
                return false;
            }
        }

        public void Close()
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
