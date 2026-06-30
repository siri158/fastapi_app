import Welcome from "./components/Welcome";
import NavBar from "./components/NavBar";
import CompanyCard from "./components/CompanyCard";
import JobCard from "./components/JobCard";
import Footer from "./components/Footer";
import { useEffect, useState } from "react";
import { getCompanies } from "./Services/CompanyService";
import type { Company } from "./types/company";

function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [companies, setCompanies] = useState<Company[]>([]);

  async function fetchCompanies() {
    setLoading(true);

    try {
      const data = await getCompanies();
      setCompanies(data);
      setError(null);
    } catch (err) {
      setError(err as Error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchCompanies();
  }, []);

  return (
    <>
      <NavBar />
      <Welcome />

      {loading && <p>Loading...</p>}

      {error && <p>{error.message}</p>}

      {!loading &&
        !error &&
        companies.map((company) => (
          <CompanyCard key={company.id} company={company} />
        ))}

      <JobCard />
      <Footer />
    </>
  );
}

export default App;