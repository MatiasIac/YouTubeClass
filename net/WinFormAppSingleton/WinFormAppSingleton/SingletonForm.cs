using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormAppSingleton
{
    public static class SingletonForm
    {
        private static readonly Form2 Instance = new Form2();

        public static Form2 Form
        {
            get
            {
                return Instance;
            }
        }
    }
}
