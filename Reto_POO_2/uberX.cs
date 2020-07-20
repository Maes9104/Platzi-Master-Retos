namespace Reto_POO_2
{
    public class uberX : iCar
    {
        private int _id;
        private int _driver_id;
        private int _model;
        private int _passengers;
        private string _brand;
        public int Id { get => _id; set => _id = value; }
        public int Driver_id { get => _driver_id; set => _driver_id = value; }
        public int Model { get => _model; set {
                if (value >= 2000)
                {
                    _model = value;
                }
            }
        }
        public int Passengers { get => _passengers; set => _passengers = value; }
        public string Brand { get => _brand; set => _brand = value; }

        public uberX(int id, int driver_id, int model, int passengers, string brand)
        {
            Id = id;
            Driver_id = driver_id;
            Model = model;
            Passengers = passengers;
            Brand = brand;
        }

        public string get_car_data()
        {
            string car_data = $@"Marca: {Brand}
            Modelo: {Model}
            Pasajeros: {Passengers}";
            return car_data;
        }

    }
}