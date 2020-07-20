namespace Reto_POO_2
{
    public abstract class Account
    {
        private int _id;
        private string _name;
        private string _lastname;
        private string _document;
        private string _email;
        private string _password;

        public int Id { get => _id; set => _id = value; }
        public string Name { get => _name; set => _name = value; }
        public string Lastname { get => _lastname; set => _lastname = value; }
        public string Document { get => _document; set => _document = value; }
        public string Email { get => _email; set => _email = value; }
        public string Password { get => _password; set => _password = value; }

        public string get_full_name(){
            return this._name + " " + this._lastname;
        }

        public abstract string get_person_data();
    }
}