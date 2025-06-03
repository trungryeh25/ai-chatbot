import logging
from typing import Dict, Any, Optional
from aiohttp import ClientSession, ClientTimeout, ClientError
import asyncio

logger = logging.getLogger("http_client")

class APICallException(Exception):
    pass


class HttpClient:
    def __init__(self, session: ClientSession):
        self.session = session

    async def request(
        self,
        url: str,
        method: str,
        headers: Optional[Dict[str, str]] = None,
        parameters: Optional[Dict[str, Any]] = None,
        is_json: bool = False,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        headers = headers or {}
        parameters = parameters or {}
        timeout_cfg = ClientTimeout(total=timeout)
        method = method.upper()

        try:
            logger.debug(
                f"[HttpClient] Calling {method} {url} "
                f"headers={headers} payload={parameters}"
            )

            kwargs = {
                "headers": headers,
                "timeout": timeout_cfg
            }

            if method in ["POST", "PUT"]:
                kwargs["json" if is_json else "params"] = parameters
            elif method in ["GET", "DELETE"]:
                kwargs["params"] = parameters
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            async with getattr(self.session, method.lower())(url, **kwargs) as response:
                response.raise_for_status()
                return await response.json()

        except ClientError as e:
            logger.error(f"HTTP error: {str(e)}")
            raise APICallException(f"HTTP error: {str(e)}")
        except asyncio.TimeoutError:
            logger.error(f"Timeout after {timeout} seconds")
            raise APICallException(f"Timeout after {timeout} seconds")
        except Exception as e:
            logger.exception(f"Unexpected error: {str(e)}")
            raise
        
    # async def close(self):
    #     if not self.session.closed:
    #         await self.session.close()
    #         logger.debug("[HttpClient] Session closed")
