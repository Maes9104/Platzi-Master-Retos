namespace Reto_POO_2
{
    public interface iCar
    {
         int Id { get; set; } 
         int Driver_id { get; set; }
         int Model { get; set; }
         int Passengers { get; set; }
         string Brand { get; set; }

         string get_car_data();

    }
}