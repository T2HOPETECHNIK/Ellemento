using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControlUI
{
    class fakeInterface
    {

        public fakeInterface(string ipAddr, int port)
        {
            Console.WriteLine("fakeInterface");
        }

        public bool init(string ipAddr)
        {
            Console.WriteLine(">> Init");
            return true;

        }   // init


        public void connect()
        {
            Console.WriteLine(">> Connect");
        }


        public bool isAvailable()
        {
            return (true);
        }


        public void disconnect()
        {
            Console.WriteLine(">> Disconnect");
        }


        public void setRegister(ushort addr, ushort value)
        {
            Console.WriteLine(addr.ToString() + " <== " + value.ToString() );
        }



        public ushort getRegister(ushort addr)
        {
            Console.WriteLine(">> getRegister " + addr.ToString());
            return (100);
        }


        public void setCoil(ushort addr, ushort bitpos, bool bval)
        {
            Console.WriteLine(addr.ToString() + " <== " + (bval?"True":"False"));
        }


        public bool getCoil(ushort addr, ushort bitpos)
        {
            Console.WriteLine("Get coil: " + addr.ToString());

            return (true);
        }


    }
}
