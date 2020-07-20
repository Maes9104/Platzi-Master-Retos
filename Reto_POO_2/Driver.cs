namespace Reto_POO_2
{
    public class Driver : Account
    {
        private string _licence_number;
        public string Licence_number { get => _licence_number; set => _licence_number = value; }
        public Driver(int id, string name, string lastname, string document, string licence_number)
        {
            Id = id;
            Name = name;
            Lastname = lastname;
            Document = document;
            Licence_number = licence_number;
        }
        public override string get_person_data()
        {
            string person_data = $@"Nombre: {this.get_full_name()}
            Documento: {this.Document}
            Email: {this.Email}
            Licencia: {this.Licence_number}";
            return person_data;
        }
    }
}