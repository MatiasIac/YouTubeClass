# Stream 07/01/2020 (NZ time)

Usaremos este directorio para colocar todo lo que hagamos durante
el stream.

Para poder aportar y participar, deberán clonar o hacer un fork del repositorio, para luego crear pull requests y así poder incorporar cambios o código en el que trabajaremos juntos.

## Links de lo conversado
- Patrones de diseño: https://www.dofactory.com/net/design-patterns
- Uno de mis repos con algunos patrones para diferentes lenguajes: https://github.com/MatiasIac/MyGeneralLearnings
- Otro de mis repos con el framework para desarrollar videojuegos con JavaScript y HTML5: https://github.com/MatiasIac/jsGFwk
- Link random de mi libro: https://www.amazon.com/Programaci%C3%B3n-Videojuegos-Desarrolla-proyecto-JavaScript-ebook/dp/B01I24QVKI

## Algunas consideraciones

Recuerden que con el tema libro, yo no gano dinero, por lo que es de total libertad por parte de ustedes comprarlo si así lo consideran. La idea de comentarlo no es para darle promoción sino para simplemente comentar que existe material en castellano :)

## Código creado

El siguiente es una implementación MUY rústica del patrón "cadena de responsabilidad".

```csharp
public abstract class Element
{
    public Element Next { get; set; }

    public abstract void Validate(string password);
}

public class ValidarMax : Element
{
    public override void Validate(string password)
    {
        if (password.Length <= 50)
        {
            if (Next != null)
            {
                Next.Validate(password);
            }
        }
        else
        {
            throw new Exception("Es muy largo!");
        }
    }
}

public class ValidarMin : Element
{
    public override void Validate(string password)
    {
        if (password.Length > 5)
        {
            if (Next != null)
            {
                Next.Validate(password);
            }
        }
        else
        {
            throw new Exception("Es muy corto!");
        }
    }
}

public class ValidarDigito : Element
{
    public override void Validate(string password)
    {
        var ok = false;
        foreach (var c in password)
        {
            if (Char.IsDigit(c))
            {
                ok = true;
                break;
            }
        }

        if (ok)
        {
            if (Next != null)
            {
                Next.Validate(password);
            }
        } 
        else
        {
            throw new Exception("No tiene numeros");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        var password = "123456";

        var max = new ValidarMax();
        var min = new ValidarMin();
        var digit = new ValidarDigito();

        //max.Next = min;
        min.Next = digit;
        digit.Next = max;

        try
        {
            max.Validate(password);
            Console.WriteLine("Todo Ok");
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
        
    }
}
```