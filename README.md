# PyFlick
A quick and dirty Python API for [Flick Electric](https://flickelectric.co.nz).

**Don't be evil** - This library has been designed to minimize hitting the Flick API as much as possible by caching data in files for later retrieval. Be a #cleverflickster and make sure you are respectful and responsible when consuming this API.

### Getting Started

First things first, clone the repo:

```bash
git clone git@github.com:driannaude/PyFlick.git
```

You will need to create a JSON config file in `src/` called config.json that contains your `username`, `password`, `client_id` and `client_secret`:
You can use the client id/secret below, or find your own by sniffing the request from your phone/app with any reputable MITM tool
```json
{
  "client_id": "le37iwi3qctbduh39fvnpevt1m2uuvz",
  "client_secret": "ignwy9ztnst3azswww66y9vd9zt6qnt",
  "username": "email@example.com",
  "password": "SuperSecretPassword"
}
```

You can then initialize the API like this:

```python
config = Config().get()
api = FlickApi(config["username"], config["password"], config["client_id"], config["client_secret"])
```

Alternatively, you can manually pass in your credentials as arguments to the FlickAPI class init method.

### Usage

The following methods are available:

|Method |Arguments |Returns |
|-------|----------|:--------|
|`getRawData()`| `None`| `Returns` Raw `JSON` object ([see below](#raw-json-data)) |
|`getPricePerKwh()`| `None`| `Returns` Price Per KwH |
|`getPriceBreakdown()`| `None`| `Returns` dict with Charges and price|
|`getLastUpdateTime()`| `Bool isEpoch` | `Returns` last updated timestamp, pass `True` value for `isEpoch` to get UTC seconds since Epoch |
|`getNextUpdateTime()`| `Bool isEpoch` | `Returns` next update timestamp, pass `True` value for `isEpoch` to get UTC seconds since Epoch | |


### Raw JSON Data
this will return a price object that looks a little like this:

```json
{
  "kind": "mobile_provider_price",
  "customer_state": "active",
  "needle": {
    "price": "19.862",
    "status": "urn:flick:market:price:forecast",
    "unit_code": "cents",
    "per": "kwh",
    "start_at": "2017-09-08T03:30:00Z",
    "end_at": "2017-09-08T03:59:59Z",
    "now": "2017-09-08T03:53:34.985Z",
    "type": "rated",
    "charge_methods": ["kwh", "spot_price"],
    "components": [{
      "charge_method": "kwh",
      "value": "0.113"
    }, {
      "charge_method": "kwh",
      "value": "1.5"
    }, {
      "charge_method": "kwh",
      "value": "10.773"
    }, {
      "charge_method": "spot_price",
      "value": "7.476"
    }]
  }
}
```

### Disclaimer/Legal
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

